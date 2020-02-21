"""[Locators]
"""
from selenium.webdriver.common.by import By


class Locators:
    """[Locators]
    """
    i_search = (By.ID, 'searchInput')
    search_button = (By.XPATH, '//*[@id="search-form"]/fieldset/button')
