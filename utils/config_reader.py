import configparser
import os


class ConfigReader:

    def __init__(self):
        self.locator_config = configparser.ConfigParser()
        self.data_config = configparser.ConfigParser()

        locator_path = os.path.join("config", "locator.ini")
        data_path = os.path.join("config", "data.ini")

        self.locator_config.read(locator_path)
        self.data_config.read(data_path)

    def get_locator(self, section, key):
        try:
            return self.locator_config.get(section, key)
        except Exception as e:
            raise Exception(f"Locator not found: [{section}] {key} -> {e}")



    def get_data(self, section, key):
        try:
            return self.data_config.get(section, key)
        except Exception as e:
            raise Exception(f"Data not found: [{section}] {key} -> {e}")
