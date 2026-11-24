
from src.lead import Lead
from src.scoring import calculate_lead_score


def qualify_lead(lead: Lead, ai_analysis: dict) -> dict:
    """Qualify a validated lead using AI analysis and Python scoring."""

    required_fields = {
        "budget_category",
        "urgency",
        "business_need"
    }

    if not required_fields.issubset(ai_analysis):
        raise ValueError("AI analysis is missing required fields.")

    result = calculate_lead_score(
        budget=ai_analysis["budget_category"],
        urgency=ai_analysis["urgency"],
        business_need=ai_analysis["business_need"]
    )

    return {
        "name": lead.name,
        "email": str(lead.email),
        "business_name": lead.business_name,
        "service_needed": lead.service_needed,
        "budget_category": ai_analysis["budget_category"],
        "urgency": ai_analysis["urgency"],
        "business_need": ai_analysis["business_need"],
        "score": result["score"],
        "category": result["category"]
    }
