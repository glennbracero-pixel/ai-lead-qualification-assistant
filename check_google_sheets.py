
from src.google_sheets import connect_to_google_sheets


def main():
    print("Connecting to Google Sheets...")

    worksheet = connect_to_google_sheets()

    print("\nGoogle Sheets connection successful!")
    print(f"Worksheet: {worksheet.title}")
    print(f"Column headings: {worksheet.row_values(1)}")


if __name__ == "__main__":
    main()
