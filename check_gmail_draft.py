
from src.gmail_client import create_gmail_service
from src.gmail_drafts import create_gmail_draft


print("Connecting to Gmail...")

service = create_gmail_service()

print("Creating test email draft...")

draft_id = create_gmail_draft(
    service=service,
    recipient="test@example.com",
    subject="TEST - AI Lead Qualification Assistant",
    body=(
        "Hello,\n\n"
        "This is a test email draft created by "
        "the AI Lead Qualification Assistant.\n\n"
        "This message has NOT been sent.\n\n"
        "Best regards,\n"
        "Digital Growth Agency"
    )
)

print("\nGmail draft created successfully!")
print("Draft ID:", draft_id)
print("The email has NOT been sent.")
