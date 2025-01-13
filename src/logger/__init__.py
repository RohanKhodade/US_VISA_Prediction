import logging
import os
from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'US_VISA_Prediction/logs'

# Correct the logs path construction
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Ensure the log directory exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Set up the logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logging.debug("Logging setup complete")
