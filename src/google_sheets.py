
import logging
import time

import gspread
import requests
from google.auth.exceptions import TransportError


CREDENTIALS_FILE = "credentials.json"

# Keep your existing Google Sheet ID here.
SPREADSHEET_ID = "1m6HimdkUgyhLllgCA_VhUKFsu3Xi42fVgCofbadDCwE"

WORKSHEET_NAME = "Leads"

logger = logging.getLogger("lead_automation")

MAX_RETRIES = 3
RETRY_DELAYS = [1, 2, 4]


def connect_to_google_sheets():
    """Connect to Google Sheets using a service account."""

    client = gspread.service_account(
        filename=CREDENTIALS_FILE
    )

    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

    return worksheet


def is_retryable_error(error):
    """Check whether an error is likely temporary."""

    if isinstance(
        error,
        (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            TransportError
        )
    ):
        return True

    if isinstance(error, gspread.exceptions.APIError):
        status_code = getattr(
            error.response,
            "status_code",
            None
        )

        return status_code in (429, 500, 502, 503, 504)

    return False


def save_lead_to_sheet(result: dict):
    """Save a lead with duplicate checking and automatic retries."""

    new_email = result["email"].strip().lower()

    row = [
        result["name"],
        result["email"],
        result["business_name"],
        result["service_needed"],
        result["budget_category"],
        result["urgency"],
        result["business_need"],
        result["score"],
        result["category"]
    ]

    for attempt in range(MAX_RETRIES + 1):

        try:
            worksheet = connect_to_google_sheets()

            # Check for duplicates before attempting to save.
            existing_emails = worksheet.col_values(2)

            for email in existing_emails[1:]:
                if email.strip().lower() == new_email:
                    print(
                        f"Duplicate lead skipped: {result['name']} "
                        f"({new_email})"
                    )

                    logger.info(
                        "Duplicate lead skipped: %s",
                        result["name"]
                    )

                    return False

            # Save the new lead.
            worksheet.append_row(
                row,
                value_input_option="USER_ENTERED"
            )

            print(
                f"Lead saved to Google Sheets: {result['name']}"
            )

            logger.info(
                "Lead saved to Google Sheets: %s",
                result["name"]
            )

            return True

        except Exception as error:

            # Do not retry errors that are unlikely to be temporary.
            if not is_retryable_error(error):
                logger.exception(
                    "Non-retryable Google Sheets error."
                )
                raise

            if attempt >= MAX_RETRIES:
                logger.exception(
                    "Google Sheets failed after %s attempts.",
                    MAX_RETRIES + 1
                )
                raise

            delay = RETRY_DELAYS[attempt]

            logger.warning(
                "Google Sheets temporary error. "
                "Retry %s of %s in %s seconds. Error: %s",
                attempt + 1,
                MAX_RETRIES,
                delay,
                error
            )

            print(
                f"Temporary Google Sheets error. "
                f"Retrying in {delay} seconds..."
            )

            time.sleep(delay)

    return False

# Google Form Responses spreadsheet
FORM_RESPONSES_SPREADSHEET_ID = "1UNKW85SOf0ytD9bmEUYLUfMpFKaJJ3i64iJFQyusNro"


def connect_to_form_responses():
    """Connect to the Google Form Responses spreadsheet."""

    client = gspread.service_account(
        filename=CREDENTIALS_FILE
    )

    spreadsheet = client.open_by_key(
        FORM_RESPONSES_SPREADSHEET_ID
    )

    worksheet = spreadsheet.sheet1

    return worksheet