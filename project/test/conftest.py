import pytest

import sys

sys.path.append("./")

from core.common.base.driver import DriverSetup
from core.utils.driverutils import DriverUtils
import unittest

# Instance of used clasess
DriverUtils = DriverUtils()
DriverSetup = DriverSetup()


@pytest.fixture
def driver():
    DriverSetup.setup()

    # # Getting driver
    driver = DriverSetup.driver
    return driver
