
import pytest
from pydantic import ValidationError

from src.lead import Lead


def test_valid_lead():
    lead = Lead(
        name="Sarah Johnson",
        email="sarah@example.com",
        business_name="Sarah's Clothing Store",
        service_needed="SEO",
        budget="$1,000-$2,000",
        message="I want to improve my online store's visibility."
    )

    assert lead.name == "Sarah Johnson"


def test_invalid_email():
    with pytest.raises(ValidationError):
        Lead(
            name="Sarah Johnson",
            email="not-an-email",
            business_name="Sarah's Clothing Store",
            service_needed="SEO",
            budget="$1,000-$2,000",
            message="I want to improve my online store's visibility."
        )
