
from src.email_generator import generate_follow_up_email


test_lead = {
    "name": "Daniel Smith",
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


print("Generating personalized follow-up email...")

email = generate_follow_up_email(
    lead=test_lead,
    customer_message=customer_message
)

print("\n===== GENERATED EMAIL =====")
print("Subject:", email["subject"])
print("\nEmail body:")
print(email["body"])
print("===========================")
