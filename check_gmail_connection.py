
from src.gmail_client import create_gmail_service


print("Connecting to Gmail...")

try:
    service = create_gmail_service()

    print("Gmail connection created successfully!")

except Exception as error:
    print("Gmail connection failed.")
    print("Error type:", type(error).__name__)
    print("Check your Google OAuth configuration.")

