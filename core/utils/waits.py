"""[Waits Utils]
"""
from core.common.base.driver import DriverSetup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
import logging


class Waits:
    """[Driver Utils Class]
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_to_be_clickable(self, by_locator):
        """[Wait for an element to be visible and clickable]

        Arguments:
            by_locator {[Locator]} -- [ex. (By.ID, "search")]
            driver {[webdriver]} -- [description]
        """
        try:
            logging.info(f"Waiting for element by {by_locator[0]} and value is {by_locator[1]} to be clickable. "
                         f"Timeout in 20 seconds")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(by_locator))
            logging.info(f"Element {by_locator[1]} was found")
        except TimeoutException:
            logging.error(f"Element {by_locator[1]} Not found")
            self.driver.close()
            self.driver.quit()
