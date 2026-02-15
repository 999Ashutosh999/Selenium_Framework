import os

class Screenshot:
    @staticmethod
    def capture(driver, name):
        path = f"reports/screenshots/{name}.png"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        driver.save_screenshot(path)