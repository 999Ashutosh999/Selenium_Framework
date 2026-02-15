# crate a class for logs that displays logs in realtime in terminal and save the logs in reports/logs/test.log
import logging
import os

class Logger:

    @staticmethod
    def get_logger():
        logger = logging.getLogger("Selenium_Framework")
        logger.setLevel(logging.DEBUG)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(os.path.join("reports", "logs", "test.log"))
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        if not logger.hasHandlers():
            logger.addHandler(c_handler)
            logger.addHandler(f_handler)

        return logger