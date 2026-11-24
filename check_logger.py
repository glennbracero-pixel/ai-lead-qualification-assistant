
from src.logger_config import setup_logger


def main():
    logger = setup_logger()

    logger.info("Lead Qualification Assistant started.")
    logger.warning("This is a test warning.")
    logger.error("This is a test error.")

    print("\nLogging test completed.")


if __name__ == "__main__":
    main()
