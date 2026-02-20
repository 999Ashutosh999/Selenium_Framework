from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.config_reader import ConfigReader
from utils.logger import Logger
from utils.screenshot import Screenshot

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger()
        self.config = ConfigReader()

    def click(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
            self.logger.info(f"Clicked element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error clicking element: {locator} - {e}")
            Screenshot.capture(self.driver, "click_error")
            raise

    def send_keys(self, by, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, locator))
            )
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Sent keys to element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error sending keys to element: {locator} - {e}")
            Screenshot.capture(self.driver, "send_keys_error")
            raise

    def get_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            text = element.text
            self.logger.info(f"Got text from element: {locator}")
            return text
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error getting text from element: {locator} - {e}")
            Screenshot.capture(self.driver, "get_text_error")
            raise

    def wait_for_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element located: {locator}")
        except TimeoutException as e:
            self.logger.error(f"Error waiting for element: {locator} - {e}")
            Screenshot.capture(self.driver, "wait_for_element_error")
            raise


    def get_locator(self, locator_strategy, locator_value):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(
                EC.presence_of_element_located((locator_strategy, locator_value))
            )
            return element
        except Exception as e:
            raise