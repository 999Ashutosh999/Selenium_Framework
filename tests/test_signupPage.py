import pytest
from selenium.webdriver.common.by import By
from pages.signup_page import SignUpPage

@pytest.mark.usefixtures("driver")
class TestSignUpPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.signup = SignUpPage(driver)
        self.signup.click(By.XPATH,self.signup.config.read_locator("home_page", "signup_login_link_xpath"))
    
    def test_signup(self):
        self.signup.signup()

    def test_login(self):   
        self.signup.login()