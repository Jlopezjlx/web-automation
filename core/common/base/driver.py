"""
Driver
"""

import sys

sys.path.append("./")

from selenium import webdriver

# Importing own Modules

from core.configs.browser_configs import BrowserConfigs

# Classes

BrowserConfigs = BrowserConfigs()


class DriverSetup:
    """[Setup Class]

    Raises:
        Exception: [Selected Browser not Supported]
    """
    def setup(self):
        """[Setup]

        Raises:
            Exception: [Selected Browser not Supported]
        """
        if BrowserConfigs.browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=BrowserConfigs.firefox_driver_path)
        elif BrowserConfigs.browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=BrowserConfigs.chrome_driver_path)
        else:
            raise Exception("Selected Browser not Supported")


if __name__ == '__main__':
    print("")
