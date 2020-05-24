"""[Youtube Home]
"""
import sys

sys.path.append("./")

from core.common.base.driver import DriverSetup
from project.locators.locators import Locators
from core.utils.driverutils import DriverUtils
import unittest
import allure
import pytest

DriverUtils = DriverUtils()
DriverSetup = DriverSetup()


class WikiHome:
    """[Home Class]
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step('{0}')
    def getting_page(self):
        """[Getting youtube home page]
        """
        try:
            self.driver.get("https://www.wikipedia.org/")
            self.driver.maximize_window()
            DriverUtils.wait_for(by_locator=Locators.i_search, driver=self.driver)
        except:
            self.tearDown()

    @allure.step('{0}')
    def type_in_search(self, text):
        """[Type in search input]

        Arguments:
            text {[str]} -- [text to be type]
        """
        try:
            self.driver.find_element(*Locators.i_search).send_keys(text)
        except:
            self.tearDown()

    @allure.step('{0}')
    def click_on_search_button(self, ):
        try:
            self.driver.find_element(*Locators.search_button).click()
        except:
            self.tearDown()


if __name__ == '__main__':
    pass
