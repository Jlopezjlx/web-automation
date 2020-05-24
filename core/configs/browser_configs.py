"""Browser Configs
"""

import sys

sys.path.append("./")


class BrowserConfigs:
    """[Browser Configurations]
    """
    browser = "chrome"
    remote = True
    chrome_driver_path = "./core/configs/chromedriver/chromedriver.exe"
    firefox_driver_path = "./core/configs/firefoxdriver/geckodriver"
