
from src.form_reader import get_latest_form_response


def main():
    print("Reading latest Google Form submission...")

    response = get_latest_form_response()

    if response:
        print("\n===== FORM RESPONSE =====")
        for field, value in response.items():
            print(f"{field}: {value}")

        print("=========================")


if __name__ == "__main__":
    main()
