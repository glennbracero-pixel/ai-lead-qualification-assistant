
import pytest

from src.scoring import calculate_lead_score


def test_hot_lead():
    result = calculate_lead_score("high", "urgent", "clear")

    assert result["score"] == 100
    assert result["category"] == "Hot"


def test_warm_lead():
    result = calculate_lead_score("medium", "soon", "unclear")

    assert result["score"] == 50
    assert result["category"] == "Warm"


def test_cold_lead():
    result = calculate_lead_score("low", "later", "unclear")

    assert result["score"] == 30
    assert result["category"] == "Cold"


def test_unknown_budget():
    result = calculate_lead_score("unknown", "urgent", "clear")

    assert result["score"] == 70
    assert result["category"] == "Warm"


def test_invalid_budget():
    with pytest.raises(ValueError):
        calculate_lead_score("unlisted", "urgent", "clear")


def test_invalid_urgency():
    with pytest.raises(ValueError):
        calculate_lead_score("high", "unknown", "clear")


def test_invalid_business_need():
    with pytest.raises(ValueError):
        calculate_lead_score("high", "urgent", "unknown")
