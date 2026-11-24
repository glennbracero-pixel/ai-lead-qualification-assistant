
import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3.5:4b"


BUDGET_MAPPING = {
    "Under $1,000": "low",
    "$1,000–$1,999": "medium",
    "$2,000 or more": "high",
    "Not sure yet": "unknown"
}


def analyze_lead_message(message: str, budget: str) -> dict:
    """Analyze a lead's message and use their selected budget."""

    budget_category = BUDGET_MAPPING.get(budget.strip())

    if budget_category is None:
        raise ValueError("Invalid budget selection from Google Forms.")

    prompt = f"""
Analyze this customer message:

{message}

Return a JSON object with exactly these two fields:

- urgency: urgent, soon, or later
- business_need: clear or unclear

URGENCY RULES:
- urgent: the customer explicitly needs help immediately
- soon: the customer needs help within 30 days
- later: no immediate or near-term deadline is stated

BUSINESS NEED RULES:
- clear: the customer explains a specific business problem or goal
- unclear: the customer's needs are too vague to identify

Do not invent information.
Return JSON only. No explanations.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "format": "json",
            "stream": False,
            "think": False,
            "options": {
                "temperature": 0,
                "num_predict": 256
            }
        },
        timeout=300
    )

    response.raise_for_status()

    result = response.json()
    response_text = result.get("response", "").strip()

    if not response_text:
        raise ValueError(
            "Ollama returned an empty response. "
            f"Completion reason: {result.get('done_reason', 'unknown')}"
        )

    analysis = json.loads(response_text)

    allowed_values = {
        "urgency": {"urgent", "soon", "later"},
        "business_need": {"clear", "unclear"}
    }

    for field, valid_values in allowed_values.items():
        if analysis.get(field) not in valid_values:
            raise ValueError(f"AI returned an invalid value for {field}.")

    return {
        "budget_category": budget_category,
        "urgency": analysis["urgency"],
        "business_need": analysis["business_need"]
    }
