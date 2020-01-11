"""Browser Configs
"""

import sys

sys.path.append("./")


class BrowserConfigs:
    """[Browser Configurations]
    """
    browser = "chrome"
    main_url = "www.google.com"
    chrome_driver_path = "./core/configs/chromedriver/chromedriver.exe"
    firefox_driver_path = "./core/configs/firefoxdriver/geckodriver.exe"
