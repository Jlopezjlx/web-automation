"""[Elements Utils]
"""
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)


class ElementsUtils:
    """[Driver Utils Class]
    """
    def __init__(self, driver):
        self.driver = driver

    def find_element_and_type(self, by_locator, text: str):
        """[Wait for an element to be visible and clickable]

        Arguments:
            by_locator {[Locator]} -- [ex. (By.ID, "search")]
            text {[str]} -- [Text to be type]
        """
        try:
            logger.info(f"Looking for element by {by_locator[0]} and value is {by_locator[1]} and when find it type {text}")
            elm = self.driver.find_element(*by_locator)
            elm.send_keys(text)
            elm = self.driver.find_element(*by_locator)
            logger.info(f"Element {by_locator[1]} was found and current value is {elm.text}")
        except TimeoutException:
            logger.error(f"Element {by_locator[1]} Not found")

    def click_on_element(self, by_locator):
        try:
            logger.info(f"Looking for element by {by_locator[0]} and value is {by_locator[1]}")
            self.driver.find_element(*by_locator).click()
            logger.info(f"Click on element {by_locator[1]} was ")
        except TimeoutException:
            logger.error(f"Element {by_locator[1]} Not found")
