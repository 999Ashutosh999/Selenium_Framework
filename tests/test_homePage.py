import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.home_page = HomePage(driver)

    def test_verify_logo(self):
        self.home_page.verifyLogo()

    @pytest.mark.parametrize("nav_locator", ["home_link_xpath", "product_link_xpath",
                                              "cart_link_xpath", "signup_login_link_xpath",
                                              "test_cases_link_xpath", "api_testing_link_xpath",
                                              "video_link_xpath", "contact_us_link_xpath"])
    def test_verify_navigation(self, nav_locator):
        self.home_page.verifyNavigation(nav_locator)