from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.config = ConfigReader()

    def verifyLogo(self):
        logo_locator = self.config.get_locator("home_page", "logo_button_xpath")
        if self.driver.find_element(By.XPATH, logo_locator).is_displayed():
            self.logger.info("Logo is displayed on the home page.")
        else:
    
            self.logger.error("Logo is not displayed on the home page.")
            
        
    