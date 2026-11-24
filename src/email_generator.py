
import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3.5:4b"


def generate_follow_up_email(
    lead: dict,
    customer_message: str
) -> dict:
    """Generate a personalized follow-up email using local AI."""

    prompt = f"""
You are a professional customer follow-up assistant
for Digital Growth Agency.

Write a friendly, professional follow-up email.

CUSTOMER INFORMATION:
Name: {lead['name']}
Business: {lead['business_name']}
Interested service: {lead['service_needed']}
Original customer message: {customer_message}

RULES:
- Address the customer by their first name.
- Mention their business and requested service.
- Acknowledge their specific goal from their original message.
- Suggest discussing their needs in a scheduled meeting.
- Do not invent prices or service details.
- Do not promise rankings, leads, sales, or traffic.
- Do not claim the consultation is free or paid.
- Keep the email concise and professional.
- Do not use placeholders such as "Your Name".
- Sign off with "Digital Growth Agency".
- Return only the email body.
- Do not include a subject line.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "options": {
                "temperature": 0.2,
                "num_predict": 400
            }
        },
        timeout=300
    )

    response.raise_for_status()

    result = response.json()
    email_body = result.get("response", "").strip()

    if not email_body:
        raise ValueError("AI returned an empty email.")

    if "your name" in email_body.lower():
        raise ValueError("AI generated an unfinished name placeholder.")

    return {
        "subject": f"Following up on your {lead['service_needed']} inquiry",
        "body": email_body
    }
