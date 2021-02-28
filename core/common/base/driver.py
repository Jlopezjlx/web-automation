"""
Driver
"""

import sys

sys.path.append("./")

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
import pytest

# Importing own Modules

from core.configs.browser_configs import BrowserConfigs

logger = logging.getLogger(__name__)

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
                try:
                    logger.info("Starting remote webdriver with Firefox")
                    self.driver = webdriver.Remote(command_executor='http://192.168.0.9:4444/wd/hub',
                                                   desired_capabilities=DesiredCapabilities.FIREFOX)
                    logger.info("Webdriver using Firefox was successfully started")
                except:
                    logger.error("Starting Remote webdriver with Firefox FAILED")
            else:
                try:
                    logger.info("Starting webdriver on Firefox locally")
                    self.driver = webdriver.Firefox(executable_path=BrowserConfigs.firefox_driver_path)
                    logger.info("Webdriver using Firefox was successfully started")
                except:
                    logger.error("Starting local webdriver with Firefox FAILED")
        elif BrowserConfigs.browser == "chrome":
            if BrowserConfigs.remote:
                try:
                    logger.info("Starting remote webdriver with Chrome")
                    self.driver = webdriver.Remote(command_executor='http://192.168.0.9:4444/wd/hub',
                                                   desired_capabilities=DesiredCapabilities.CHROME)
                    logger.info("Webdriver using Chrome was successfully started")
                except:
                    logger.error("Starting Remote webdriver with Chrome FAILED")
            else:
                try:
                    logger.info("Starting webdriver with Chrome locally")
                    self.driver = webdriver.Chrome(executable_path=BrowserConfigs.chrome_driver_path)
                    logger.info("Webdriver using Chrome was successfully started")
                except:
                    logger.error("Starting local webdriver with Chrome FAILED")
        else:
            raise Exception("Selected Browser not Supported")


if __name__ == '__main__':
    print("")
