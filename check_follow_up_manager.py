
from src.follow_up_manager import create_lead_follow_up_draft


test_lead = {
    "name": "Daniel Smith",
    "email": "test@example.com",
    "business_name": "Daniel's Fitness Studio",
    "service_needed": "Social Media Marketing",
    "budget_category": "medium",
    "urgency": "soon",
    "business_need": "clear"
}

customer_message = (
    "I recently opened a fitness studio. "
    "I want to attract more local customers through "
    "social media and would like to start within "
    "the next 30 days."
)


print("Generating email and creating Gmail draft...")

result = create_lead_follow_up_draft(
    lead=test_lead,
    customer_message=customer_message
)

print("\n===== FOLLOW-UP DRAFT CREATED =====")
print("Recipient:", result["recipient"])
print("Subject:", result["subject"])
print("Draft ID:", result["draft_id"])
print("Status: Draft created, not sent.")
print("===================================")
