from pages.home_page import HomePage

class TestHomePage:
    def test_verify_logo(self, driver):
        home_page = HomePage(driver)
        home_page.verifyLogo()

    def test_logger(self, driver):
        home_page = HomePage(driver)
        home_page.logger.info("test")