"""[Test Youtube]
"""
import sys

sys.path.append("./")

import time
import unittest
import allure
import pytest

from project.pages.wikihome import WikiHome

# Instance of used classes
WikiHome = WikiHome()


class TestWiki(unittest.TestCase):
    """[Test Wiki Home]
    """
    def test_wiki(self):
        """[Home]
        """

        # Getting Home Page
        try:
            WikiHome.getting_page()
        except:
            self.fail("Error on loading page")

        # Type in search
        try:
            WikiHome.type_in_search("Chuky73")
        except:
            self.fail("Error on type in")

        time.sleep(2)

        # Closing and Quiting
        WikiHome.tearDown()


if __name__ == '__main__':
    unittest.main()
