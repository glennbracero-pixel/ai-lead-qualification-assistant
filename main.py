
from src.ai_analyzer import analyze_lead_message
from src.qualification import qualify_lead
from src.google_sheets import save_lead_to_sheet
from src.form_reader import (
    get_pending_validated_leads,
    update_form_response_status
)
from src.follow_up_manager import create_lead_follow_up_draft
from src.logger_config import setup_logger


logger = setup_logger()


def process_customer(lead):
    """Analyze, qualify, save, and prepare a follow-up draft."""

    logger.info("Processing lead: %s", lead.name)

    print(f"\nAnalyzing lead: {lead.name}...")

    # Step 1: Analyze the customer's message
    ai_analysis = analyze_lead_message(
        message=lead.message,
        budget=lead.budget
    )

    # Step 2: Calculate the lead score
    result = qualify_lead(
        lead=lead,
        ai_analysis=ai_analysis
    )

    logger.info(
        "Lead qualified: %s | Score: %s | Category: %s",
        lead.name,
        result["score"],
        result["category"]
    )

    # Step 3: Display the qualification result
    print("\n===== LEAD QUALIFICATION RESULT =====")
    print(f"Name: {result['name']}")
    print(f"Business: {result['business_name']}")
    print(f"Budget category: {result['budget_category']}")
    print(f"Urgency: {result['urgency']}")
    print(f"Business need: {result['business_need']}")
    print(f"Lead Score: {result['score']}/100")
    print(f"Lead Category: {result['category']}")
    print("=====================================")

    # Step 4: Save the lead to the CRM
    saved = save_lead_to_sheet(result)

    if not saved:
        logger.info("Duplicate lead skipped: %s", lead.name)
        print("Duplicate lead. No new email draft created.")
        return "Duplicate"

    logger.info("New lead saved: %s", lead.name)

    # Step 5: Generate and create a Gmail follow-up draft
    try:
        print("\nGenerating follow-up email draft...")

        draft = create_lead_follow_up_draft(
            lead=result,
            customer_message=lead.message
        )

        logger.info(
            "Gmail draft created for %s. Draft ID: %s",
            lead.name,
            draft["draft_id"]
        )

        print("\n===== GMAIL DRAFT CREATED =====")
        print(f"Recipient: {draft['recipient']}")
        print(f"Subject: {draft['subject']}")
        print("Status: Saved as a draft. Not sent.")
        print("================================")

        return "Processed"

    except Exception:
        logger.exception(
            "Lead saved, but Gmail draft creation failed for %s.",
            lead.name
        )

        print(
            "Lead saved successfully, but the Gmail draft "
            "could not be created. Check logs/automation.log."
        )

        return "Processed - Draft Failed"


def main():
    logger.info("Lead Qualification Assistant started.")

    try:
        # Step 1: Find pending form submissions
        pending_leads = get_pending_validated_leads()

        if not pending_leads:
            print("No new submissions waiting for processing.")
            logger.info("No pending submissions found.")
            return

        print(f"\nFound {len(pending_leads)} pending submission(s).")

        # Step 2: Process each submission
        for item in pending_leads:

            row_number = item["row_number"]
            lead = item["lead"]

            try:
                status = process_customer(lead)

                # Step 3: Update the original form response
                update_form_response_status(
                    row_number,
                    status
                )

                logger.info(
                    "Form response row %s marked as %s.",
                    row_number,
                    status
                )

            except Exception:
                logger.exception(
                    "Failed to process form response row %s.",
                    row_number
                )

                print(
                    f"Could not process {lead.name}. "
                    "Check logs/automation.log."
                )

    except Exception:
        logger.exception("Failed to read pending form submissions.")
        print("Could not read form responses. Check logs/automation.log.")

    logger.info("Lead Qualification Assistant finished.")


if __name__ == "__main__":
    main()
