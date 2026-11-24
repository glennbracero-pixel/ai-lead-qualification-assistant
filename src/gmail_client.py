
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Google authorization files
CLIENT_FILE = PROJECT_ROOT / "gmail_oauth_client.json"
TOKEN_FILE = PROJECT_ROOT / "gmail_token.json"

# Request Gmail draft access
SCOPES = [
    "https://www.googleapis.com/auth/gmail.compose"
]


def create_gmail_service():
    """Authorize Gmail and create a Gmail API connection."""

    credentials = None

    # Load an existing authorization token
    if TOKEN_FILE.exists():
        credentials = Credentials.from_authorized_user_file(
            str(TOKEN_FILE),
            SCOPES
        )

    # Refresh or request authorization if necessary
    if not credentials or not credentials.valid:

        if (
            credentials
            and credentials.expired
            and credentials.refresh_token
        ):
            credentials.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_FILE),
                SCOPES
            )

            credentials = flow.run_local_server(port=0)

        # Save the new authorization token
        TOKEN_FILE.write_text(
            credentials.to_json(),
            encoding="utf-8"
        )

    # Connect to Gmail
    service = build(
        "gmail",
        "v1",
        credentials=credentials
    )

    return service
