
from src.google_sheets import connect_to_form_responses
from src.lead import Lead


def get_pending_form_responses():
    """Read all form submissions that have not been processed."""

    worksheet = connect_to_form_responses()

    records = worksheet.get_all_records()

    pending_responses = []

    for row_number, record in enumerate(records, start=2):

        status = str(
            record.get("Processing Status", "")
        ).strip().lower()

        if status in ("processed", "duplicate"):
            continue

        response = {
            "name": record["Full Name"],
            "email": record["Email Address"],
            "business_name": record["Business Name"],
            "service_needed": record[
                "Which service are you interested in?"
            ],
            "budget": record[
                "What is your approximate marketing budget?"
            ],
            "message": record[
                "Tell us about your business goals or challenges."
            ]
        }

        pending_responses.append({
            "row_number": row_number,
            "response": response
        })

    return pending_responses


def get_pending_validated_leads():
    """Validate all submissions that still need processing."""

    pending_responses = get_pending_form_responses()

    validated_leads = []

    for item in pending_responses:
        lead = Lead(**item["response"])

        validated_leads.append({
            "row_number": item["row_number"],
            "lead": lead
        })

    return validated_leads


def update_form_response_status(row_number: int, status: str):
    """Update the processing status in the Google Form Responses sheet."""

    worksheet = connect_to_form_responses()

    worksheet.update_cell(
        row_number,
        8,
        status
    )
