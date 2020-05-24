"""[Test Youtube]
"""
import sys

sys.path.append("./")

import time
import unittest
import allure
import pytest

from project.pages.wikihome import WikiHome


def test_wiki(driver):
    """[Home]
    """

    wiki_home = WikiHome(driver)
    # Getting Home Page
    wiki_home.getting_page()
    # Type in search
    wiki_home.type_in_search("Chuky73")
    wiki_home.click_on_search_button()
    time.sleep(2)
    # Closing and Quiting
    wiki_home.tearDown()


def test_wiki_second(driver):
    """[Home]
    """

    wiki_home = WikiHome(driver)
    # Getting Home Page
    wiki_home.getting_page()
    # Type in search
    wiki_home.type_in_search("Chuky73")
    wiki_home.click_on_search_button()
    time.sleep(2)
    # Closing and Quiting
    wiki_home.tearDown()


if __name__ == '__main__':
    unittest.main()
