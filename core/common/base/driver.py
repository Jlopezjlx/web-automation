"""
Driver
"""

import sys

sys.path.append("./")

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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
            if BrowserConfigs.remote:
                self.driver = webdriver.Remote(command_executor='http://192.168.0.9:4444/wd/hub',
                                               desired_capabilities=DesiredCapabilities.FIREFOX)
            else:
                self.driver = webdriver.Firefox(executable_path=BrowserConfigs.firefox_driver_path)
        elif BrowserConfigs.browser == "chrome":
            if BrowserConfigs.remote:
                self.driver = webdriver.Remote(command_executor='http://192.168.0.9:4444/wd/hub',
                                               desired_capabilities=DesiredCapabilities.CHROME)
            else:
                self.driver = webdriver.Chrome(executable_path=BrowserConfigs.chrome_driver_path)
        else:
            raise Exception("Selected Browser not Supported")


if __name__ == '__main__':
    print("")
