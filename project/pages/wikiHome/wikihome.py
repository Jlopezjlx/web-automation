"""[Youtube Home]
"""
import sys

sys.path.append("../")

from project.pages.wikiHome.locators import Locators
from core.utils.waits import Waits
from core.utils.elementsUtils import ElementsUtils
import allure


class WikiHome:
    """[Home Class]
    """
    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver=self.driver)
        self.elementUtils = ElementsUtils(driver=self.driver)

    def tear_down(self):
        """[Closing and quitting driver]
        """
        self.driver.close()
        self.driver.quit()

    @allure.step('{0}')
    def getting_page(self):
        """[Getting youtube home page]
        """
        try:
            self.driver.get("https://www.wikipedia.org/")
            self.driver.maximize_window()
            self.waits.wait_to_be_clickable(by_locator=Locators.i_search)
        except:
            self.tear_down()

    @allure.step('{0}')
    def type_in_search(self, text):
        """[Type in search input]

        Arguments:
            text {[str]} -- [text to be type]
        """
        try:
            self.elementUtils.find_element_and_type(
                by_locator=Locators.i_search,
                text=text
            )
        except:
            self.tear_down()

    @allure.step('{0}')
    def click_on_search_button(self):
        try:
            self.elementUtils.click_on_element(by_locator=Locators.search_button)
        except:
            self.tear_down()


if __name__ == '__main__':
    pass
