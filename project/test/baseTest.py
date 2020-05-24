import sys

sys.path.append("./")

from project.pages.wikihome import WikiHome
from core.common.base.driver import DriverSetup
from core.utils.driverutils import DriverUtils
import unittest

# Instance of used clasess
DriverUtils = DriverUtils()
DriverSetup = DriverSetup()


class BaseTest(unittest.TestCase):
    def setUp(self):
        DriverSetup.setup()
        self.driver = DriverSetup.driver
        self.home = WikiHome(self.driver)

    def tear_down(self):
        """[Closing and quitting driver]
        """
        self.driver.close()
        self.driver.quit()
