
from email.message import EmailMessage
import base64


def create_gmail_draft(service, recipient, subject, body):
    """Create a Gmail draft without sending the email."""

    message = EmailMessage()

    message["To"] = recipient
    message["Subject"] = subject

    message.set_content(body)

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    draft = service.users().drafts().create(
        userId="me",
        body={
            "message": {
                "raw": encoded_message
            }
        }
    ).execute()

    return draft["id"]
