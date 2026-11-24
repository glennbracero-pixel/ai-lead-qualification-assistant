
from enum import Enum


class LeadCategory(str, Enum):
    HOT = "Hot"
    WARM = "Warm"
    COLD = "Cold"


BUDGET_POINTS = {
    "high": 30,
    "medium": 20,
    "low": 10,
    "unknown": 0,
}

URGENCY_POINTS = {
    "urgent": 30,
    "soon": 20,
    "later": 10,
}

NEED_POINTS = {
    "clear": 40,
    "unclear": 10,
}


def calculate_lead_score(
    budget: str,
    urgency: str,
    business_need: str
) -> dict:
    """Calculate a lead score using transparent business rules."""

    budget = budget.lower().strip()
    urgency = urgency.lower().strip()
    business_need = business_need.lower().strip()

    if budget not in BUDGET_POINTS:
        raise ValueError("Invalid budget category.")

    if urgency not in URGENCY_POINTS:
        raise ValueError("Invalid urgency category.")

    if business_need not in NEED_POINTS:
        raise ValueError("Invalid business need category.")

    score = (
        BUDGET_POINTS[budget]
        + URGENCY_POINTS[urgency]
        + NEED_POINTS[business_need]
    )

    if score >= 80:
        category = LeadCategory.HOT
    elif score >= 50:
        category = LeadCategory.WARM
    else:
        category = LeadCategory.COLD

    return {
        "score": score,
        "category": category.value
    }
