
from src.google_sheets import connect_to_form_responses


def main():
    print("Connecting to Google Form Responses...")

    worksheet = connect_to_form_responses()

    print("\nConnection successful!")
    print(f"Worksheet: {worksheet.title}")
    print(f"Column headings: {worksheet.row_values(1)}")
    print(f"Number of responses: {worksheet.row_count}")


if __name__ == "__main__":
    main()
