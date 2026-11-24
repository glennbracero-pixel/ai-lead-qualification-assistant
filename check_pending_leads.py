
from src.form_reader import get_pending_validated_leads

leads = get_pending_validated_leads()

print("\n===== PENDING LEADS =====")

if not leads:
    print("No new submissions waiting for processing.")

else:
    for item in leads:
        lead = item["lead"]

        print(f"Spreadsheet row: {item['row_number']}")
        print(f"Name: {lead.name}")
        print(f"Email: {lead.email}")
        print("-------------------------")

print("=========================")
