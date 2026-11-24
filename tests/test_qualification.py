
from src.lead import Lead
from src.qualification import qualify_lead


def test_qualify_lead():
    lead = Lead(
        name="Sarah Johnson",
        email="sarah@example.com",
        business_name="Sarah's Clothing Store",
        service_needed="SEO",
        budget="$3,000",
        message="I want to improve my online store's visibility."
    )

    ai_analysis = {
        "budget_category": "high",
        "urgency": "urgent",
        "business_need": "clear"
    }

    result = qualify_lead(
        lead=lead,
        ai_analysis=ai_analysis
    )

    assert result["name"] == "Sarah Johnson"
    assert result["score"] == 100
    assert result["category"] == "Hot"
    assert result["service_needed"] == "SEO"
    assert result["budget_category"] == "high"


def test_missing_ai_analysis_field():
    lead = Lead(
        name="Sarah Johnson",
        email="sarah@example.com",
        business_name="Sarah's Clothing Store",
        service_needed="SEO",
        budget="$3,000",
        message="I want to improve my online store's visibility."
    )

    ai_analysis = {
        "budget_category": "high",
        "urgency": "urgent"
    }

    try:
        qualify_lead(lead, ai_analysis)
        assert False, "Expected ValueError"
    except ValueError as error:
        assert "missing required fields" in str(error)
