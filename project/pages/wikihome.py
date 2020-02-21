"""[Youtube Home]
"""
import sys

sys.path.append("./")

from core.common.base.driver import DriverSetup
from project.locators.locators import Locators
from core.utils.driverutils import DriverUtils
import unittest
import allure

# Instance of used clasess
DriverUtils = DriverUtils()
DriverSetup = DriverSetup()

# Setting up driver
DriverSetup.setup()

# Getting driver
driver = DriverSetup.driver


class WikiHome(unittest.TestCase):
    """[Home Class]
    """
    def tearDown(self):
        """[Closing and quitting driver]
        """
        driver.close()
        driver.quit()

    @allure.step('{0}')
    def getting_page(self):
        """[Getting youtube home page]
        """
        try:
            driver.get("https://www.wikipedia.org/")
            driver.maximize_window()
            DriverUtils.wait_for(Locators.i_search, driver)
        except:
            self.tearDown()
            self.fail("Fail on Loading Youtube Page")

    @allure.step('{0}')
    def type_in_search(self, text):
        """[Type in search input]

        Arguments:
            text {[str]} -- [text to be type]
        """
        try:
            driver.find_element(*Locators.i_search).send_keys(text)
        except:
            self.tearDown()
            self.fail("Fail on Typing search param")

    @allure.step('{0}')
    def click_on_search_button(self):
        try:
            driver.find_element(*Locators.search_button).click()
        except:
            self.tearDown()
            self.fail("Fail on clicking on search button")


if __name__ == '__main__':
    pass
