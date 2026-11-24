
import logging
from pathlib import Path


# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Create the logs folder if it doesn't exist
LOG_FOLDER = PROJECT_ROOT / "logs"
LOG_FOLDER.mkdir(exist_ok=True)

# Set the log file location
LOG_FILE = LOG_FOLDER / "automation.log"


def setup_logger():
    """Configure logging for the automation project."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("lead_automation")
