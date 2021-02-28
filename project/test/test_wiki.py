"""[Test Youtube]
"""
import logging
import sys


sys.path.append("./")

import time
import unittest
import pytest
from project.test.baseTest import BaseTest


class TestHome(BaseTest):

    def test_wiki(self):
        """[Home, This is just a placeholder, it is not a real test]
        """
        # Getting Home Page
        self.home.getting_page()
        # Type in search
        self.home.type_in_search("Chuky73")
        self.home.click_on_search_button()
        time.sleep(2)
        # Closing and Quiting
        self.tear_down()

    def test_wiki_second(self):
        """[Home, This is just a placeholder, it is not a real test]
        """
        # Getting Home Page
        self.home.getting_page()
        # Type in search
        self.home.type_in_search("Chuky73")
        self.home.click_on_search_button()
        time.sleep(2)
        # Closing and Quiting
        self.tear_down()


if __name__ == '__main__':
    pytest.main()
    unittest.main()
