
from src.email_generator import generate_follow_up_email
from src.gmail_drafts import create_gmail_draft
from src.gmail_client import create_gmail_service


def create_lead_follow_up_draft(lead: dict, customer_message: str):
    """Generate a personalized email and save it as a Gmail draft."""

    # Step 1: Generate the email using local AI
    email = generate_follow_up_email(
        lead=lead,
        customer_message=customer_message
    )

    # Step 2: Connect to Gmail
    service = create_gmail_service()

    # Step 3: Create the Gmail draft
    draft_id = create_gmail_draft(
        service=service,
        recipient=lead["email"],
        subject=email["subject"],
        body=email["body"]
    )

    return {
        "draft_id": draft_id,
        "recipient": lead["email"],
        "subject": email["subject"]
    }
