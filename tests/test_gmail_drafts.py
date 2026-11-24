
from unittest.mock import Mock

from src.gmail_drafts import create_gmail_draft


def test_create_gmail_draft():
    """Test Gmail draft creation using a simulated response."""

    fake_service = Mock()

    fake_service.users.return_value.drafts.return_value.create.return_value.execute.return_value = {
        "id": "test-draft-123"
    }

    draft_id = create_gmail_draft(
        service=fake_service,
        recipient="test@example.com",
        subject="Test Follow-Up",
        body="Hello, this is a test email."
    )

    assert draft_id == "test-draft-123"

    fake_service.users.return_value.drafts.return_value.create.assert_called_once()

    fake_service.users.return_value.drafts.return_value.create.return_value.execute.assert_called_once()
