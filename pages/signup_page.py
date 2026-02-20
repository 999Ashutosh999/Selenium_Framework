from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def signup(self):
        name_locator = self.config.read_locator("signup_page", "name_input_xpath")
        email_locator = self.config.read_locator("signup_page", "email_input_xpath")
        signup_button_locator = self.config.read_locator("signup_page", "signup_button_xpath")

        self.send_keys(By.XPATH, name_locator, self.config.get_data("signup", "name"))
        self.send_keys(By.XPATH, email_locator, self.config.get_data("signup", "email"))
        self.click(By.XPATH, signup_button_locator)
        
    def login(self):
        email_locator = self.config.read_locator("login_page", "email_input_xpath")
        password_locator = self.config.read_locator("login_page", "password_input_xpath")
        login_button_locator = self.config.read_locator("login_page", "login_button_xpath")

        self.send_keys(By.XPATH, email_locator, self.config.get_data("login", "email"))
        self.send_keys(By.XPATH, password_locator, self.config.get_data("login", "password"))
        self.click(By.XPATH, login_button_locator)