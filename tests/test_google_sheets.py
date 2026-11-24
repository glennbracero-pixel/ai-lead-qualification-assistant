
import pytest
import requests

from src.google_sheets import save_lead_to_sheet


class FakeWorksheet:
    """Simulate a Google Sheets worksheet for testing."""

    def __init__(self, existing_emails):
        self.existing_emails = existing_emails
        self.saved_rows = []

    def col_values(self, column_number):
        return self.existing_emails

    def append_row(self, row, value_input_option=None):
        self.saved_rows.append(row)


def sample_lead():
    return {
        "name": "Michael Brown",
        "email": "michael@example.com",
        "business_name": "Michael's Fitness Studio",
        "service_needed": "Social Media Marketing",
        "budget_category": "medium",
        "urgency": "soon",
        "business_need": "clear",
        "score": 80,
        "category": "Hot"
    }


def test_duplicate_lead_is_skipped(monkeypatch):
    worksheet = FakeWorksheet([
        "Email",
        "sarah@example.com"
    ])

    monkeypatch.setattr(
        "src.google_sheets.connect_to_google_sheets",
        lambda: worksheet
    )

    result = save_lead_to_sheet({
        "name": "Sarah Johnson",
        "email": "sarah@example.com",
        "business_name": "Sarah's Clothing Store",
        "service_needed": "SEO",
        "budget_category": "high",
        "urgency": "urgent",
        "business_need": "clear",
        "score": 100,
        "category": "Hot"
    })

    assert result is False
    assert len(worksheet.saved_rows) == 0


def test_new_lead_is_saved(monkeypatch):
    worksheet = FakeWorksheet(["Email"])

    monkeypatch.setattr(
        "src.google_sheets.connect_to_google_sheets",
        lambda: worksheet
    )

    result = save_lead_to_sheet(sample_lead())

    assert result is True
    assert len(worksheet.saved_rows) == 1
    assert worksheet.saved_rows[0][1] == "michael@example.com"


def test_retry_succeeds_after_temporary_failure(monkeypatch):
    worksheet = FakeWorksheet(["Email"])

    attempts = []
    delays = []

    def fake_connection():
        attempts.append(1)

        if len(attempts) == 1:
            raise requests.exceptions.ConnectionError(
                "Simulated temporary connection failure"
            )

        return worksheet

    monkeypatch.setattr(
        "src.google_sheets.connect_to_google_sheets",
        fake_connection
    )

    monkeypatch.setattr(
        "src.google_sheets.time.sleep",
        delays.append
    )

    result = save_lead_to_sheet(sample_lead())

    assert result is True
    assert len(attempts) == 2
    assert delays == [1]
    assert len(worksheet.saved_rows) == 1


def test_retry_stops_after_four_failed_attempts(monkeypatch):
    attempts = []
    delays = []

    def fake_connection():
        attempts.append(1)

        raise requests.exceptions.ConnectionError(
            "Simulated connection failure"
        )

    monkeypatch.setattr(
        "src.google_sheets.connect_to_google_sheets",
        fake_connection
    )

    monkeypatch.setattr(
        "src.google_sheets.time.sleep",
        delays.append
    )

    with pytest.raises(requests.exceptions.ConnectionError):
        save_lead_to_sheet(sample_lead())

    assert len(attempts) == 4
    assert delays == [1, 2, 4]
