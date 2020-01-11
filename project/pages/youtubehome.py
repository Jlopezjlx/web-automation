"""[Youtube Home]
"""
import sys

sys.path.append("./")

from core.common.base.driver import DriverSetup
from selenium.webdriver.common.by import By
from project.locators.youtubelocators import YoutubeLocators
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


class YoutubeHome(unittest.TestCase):
    """[Youtube Home Class]
    """
    def tearDown(self):
        """[Closing and quitting driver]
        """
        driver.close()
        driver.quit()

    @allure.step('{0}')
    def getting_youtube_page(self):
        """[Getting youtube home page]
        """
        try:
            driver.get("https://www.youtube.com/")
            driver.maximize_window()
            DriverUtils.wait_for(YoutubeLocators.b_search, driver)
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
            driver.find_element(*YoutubeLocators.i_search).send_keys(text)
        except:
            self.tearDown()
            self.fail("Fail on Typing search param")


if __name__ == '__main__':
    pass
