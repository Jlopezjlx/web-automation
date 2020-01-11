"""[Test Youtube]
"""
import sys

sys.path.append("./")

import time
import unittest
import allure
import pytest

from project.pages.youtubehome import YoutubeHome

# Instance of used classes
YoutubeHome = YoutubeHome()


class TestYoutube(unittest.TestCase):
    """[Test Youtube Home]
    """
    def test_youtube(self):
        """[Test Youtube Home]
        """

        # Getting Home Page
        try:
            YoutubeHome.getting_youtube_page()
        except:
            self.fail("Error on loading page")

        # Type in search
        try:
            YoutubeHome.type_in_search("Chuky73")
        except:
            self.fail("Error on type in")

        time.sleep(2)

        # Closing and Quiting
        YoutubeHome.tearDown()

