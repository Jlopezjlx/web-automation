"""[Reporter]
"""
from contextlib import contextmanager
from allure_commons.types import AttachmentType
import allure
import datetime


class Reporter(object):
    """[Reporter Class]
    """
    @classmethod
    def log_click(cls, locator):
        cls.log('Click on {}'.format(locator))

    @classmethod
    def log_get_text(cls, locator):
        cls.log('Getting text on {}'.format(locator))

    @classmethod
    def log_is_selected(cls, locator):
        cls.log('Getting property is_selected on {}'.format(locator))

    @classmethod
    def log_is_displayed(cls, locator):
        cls.log('Getting property is_displayed on {}'.format(locator))

    @classmethod
    def log_get_location(cls, locator):
        cls.log('Getting property location on {}'.format(locator))

    @classmethod
    def log_get_size(cls, locator):
        cls.log('Getting property size on {}'.format(locator))

    @classmethod
    def log_click_center(cls, locator):
        cls.log('Click Center on {}'.format(locator))

    @classmethod
    def log_send_keys(cls, locator):
        cls.log('Send Keys on {}'.format(locator))

    @classmethod
    def log(cls, text):
        _log(text)


@allure.step('{0}')
def _log(text):
    pass
