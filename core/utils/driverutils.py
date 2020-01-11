"""[Driver Utils]
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os


class DriverUtils(object):
    """[Driver Utils Class]
    """
    def wait_for(self, by_locator, driver):
        """[Wait for an element to be visible and clickable]

        Arguments:
            by_locator {[Locator]} -- [ex. (By.ID, "search")]
            driver {[webdriver]} -- [description]
        """
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(by_locator))
        except TimeoutException:
            print('Error, element not loaded')
            driver.close()
            driver.quit()
