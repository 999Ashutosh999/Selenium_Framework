import logging
import os

class Logger:

    @staticmethod
    def get_logger():

        logger = logging.getLogger("Selenium_Framework")
        logger.setLevel(logging.DEBUG)

        if logger.handlers:
            return logger

        # Get absolute path of this file
        current_path = os.path.abspath(__file__)

        # Split path until we reach selenium_framework
        while os.path.basename(current_path) != "selenium_framework":
            current_path = os.path.dirname(current_path)

        framework_root = current_path

        log_dir = os.path.join(framework_root, "reports", "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "test.log")

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(log_file)

        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        c_handler.setFormatter(formatter)
        f_handler.setFormatter(formatter)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        return logger
    

