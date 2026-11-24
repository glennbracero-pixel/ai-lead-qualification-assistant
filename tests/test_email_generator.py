
from unittest.mock import patch, Mock

from src.email_generator import generate_follow_up_email


def test_generate_follow_up_email():
    """Test email generation using a simulated AI response."""

    fake_response = Mock()

    fake_response.json.return_value = {
        "response": (
            "Hi Daniel,\n\n"
            "Thank you for contacting us about your fitness studio.\n\n"
            "Best regards,\n"
            "Digital Growth Agency"
        )
    }

    fake_response.raise_for_status.return_value = None

    lead = {
        "name": "Daniel Smith",
        "business_name": "Daniel's Fitness Studio",
        "service_needed": "Social Media Marketing"
    }

    with patch(
        "src.email_generator.requests.post",
        return_value=fake_response
    ) as mock_post:

        result = generate_follow_up_email(
            lead=lead,
            customer_message="I want to attract more local customers."
        )

    assert result["subject"] == (
        "Following up on your Social Media Marketing inquiry"
    )

    assert "Hi Daniel" in result["body"]

    assert "Digital Growth Agency" in result["body"]

    mock_post.assert_called_once()


def test_empty_ai_response():
    """Test that an empty AI response is rejected."""

    fake_response = Mock()

    fake_response.json.return_value = {
        "response": ""
    }

    fake_response.raise_for_status.return_value = None

    lead = {
        "name": "Daniel Smith",
        "business_name": "Daniel's Fitness Studio",
        "service_needed": "Social Media Marketing"
    }

    with patch(
        "src.email_generator.requests.post",
        return_value=fake_response
    ):

        try:
            generate_follow_up_email(
                lead=lead,
                customer_message="I want more customers."
            )

            assert False, "Expected ValueError was not raised."

        except ValueError as error:
            assert "empty email" in str(error)
