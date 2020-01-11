"""[Allure Utils]
"""
import sys

sys.path.append("./")

from core.common.base.driver import DriverSetup
from allure_commons.types import AttachmentType
import allure
import datetime

DriverSetup = DriverSetup()


class AllureUtils(object):
    """[Allure Utils Class]

    Arguments:
        object {[type]} -- [description]
    """
    def __init__(self):
        self.driver = DriverSetup.driver

    def attach_screenshot(self, driver):
        """[Attach Screenshot on allure report]

        Arguments:
            driver {[webdriver]} -- [description]
        """
        try:
            attachment_name = "screenshot {0}".format(datetime.datetime.now().isoformat())
            allure.attach(driver.get_screenshot_as_png(),
                        name=attachment_name,
                        attachment_type=AttachmentType.PNG)
        except:
            pass


if __name__ == '__main__':
    pass
