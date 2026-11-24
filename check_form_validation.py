
from src.form_reader import get_latest_validated_lead


def main():
    print("Reading and validating the latest form submission...")

    lead = get_latest_validated_lead()

    if lead:
        print("\n===== VALIDATED LEAD =====")
        print(f"Name: {lead.name}")
        print(f"Email: {lead.email}")
        print(f"Business: {lead.business_name}")
        print(f"Service: {lead.service_needed}")
        print(f"Budget: {lead.budget}")
        print(f"Message: {lead.message}")
        print("==========================")

        print("\nLead validation successful!")


if __name__ == "__main__":
    main()
