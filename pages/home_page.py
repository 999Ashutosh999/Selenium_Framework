from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyLogo(self):
        logo_locator = self.config.read_locator("home_page", "logo_button_xpath")
        if self.get_locator(By.XPATH, logo_locator).is_displayed():
            self.logger.info("Logo is displayed on the home page.")
        else:
    
            self.logger.error("Logo is not displayed on the home page.")
            
   
    def verifyNavigation(self, nav_locator):
        nav_locator = self.config.read_locator("home_page", nav_locator)
        if self.get_locator(By.XPATH, nav_locator).is_displayed():
            self.logger.info("Navigation is displayed on the home page.")
        else:
            self.logger.error("Navigation is not displayed on the home page.")