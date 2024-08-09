# src/utils/error_handler.py
import os
import logging
from datetime import datetime

class ErrorHandler:
    def __init__(self, initial_log_dir: str = "logs"):
        self.log_dir = initial_log_dir
        self.ensure_log_directory()
        self.setup_logger()

    def ensure_log_directory(self) -> None:
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def setup_logger(self) -> None:
        log_file = os.path.join(self.log_dir, f"{datetime.now().strftime('%Y%m%d')}.log")
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def update_log_directory(self, new_log_dir: str) -> None:
        self.log_dir = new_log_dir
        self.ensure_log_directory()
        self.setup_logger()

    def log_error(self, message: str, error_details: str = None) -> None:
        log_message = f"{message}"
        if error_details:
            log_message += f"\nDetails: {error_details}"
        logging.error(log_message)
        print(log_message)  # Also print to console for immediate visibility

    def log_info(self, message: str) -> None:
        logging.info(message)

    def log_debug(self, message: str) -> None:
        logging.debug(message)