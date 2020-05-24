"""[Test Youtube]
"""
import sys

sys.path.append("./")

import time
import unittest
from project.test.baseTest import BaseTest


class TestHome(BaseTest):

    def test_wiki(self):
        """[Home]
        """
        # Getting Home Page
        self.home.getting_page()
        # Type in search
        self.home.type_in_search("Chuky73")
        self.home.click_on_search_button()
        time.sleep(2)
        # Closing and Quiting
        self.home.tearDown()

    def test_wiki_second(self):
        """[Home]
        """
        # Getting Home Page
        self.home.getting_page()
        # Type in search
        self.home.type_in_search("Chuky73")
        self.home.click_on_search_button()
        time.sleep(2)
        # Closing and Quiting
        self.home.tearDown()


if __name__ == '__main__':
    unittest.main()
