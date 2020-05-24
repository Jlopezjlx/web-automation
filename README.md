# Web Automation testing

Scalable web automation framework, great configurable. 

## Tools
1. Python
2. Pytest
3. Selenium
4. Docker (to run basic selenium grid with 5 nodes)


## Notes

1. This repo is to be used in web automations.
2. Framework is configured to be able to use chrome and firefox (can be scalable to use other browsers).
3. Framework uses pytest as testing framework.
4. Framework uses allure for report.
5. Can execute a basic selenium grid with 5 nodes.


## Run

1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run grid (optional): `docker-compose -f docker-compose.yaml up`
4. Configure project:
    1. Go to: `core/configs/browser_configs.py`
    2. Select browser:   `browser = "chrome"` default is chrome
    3. Use grid or not: `remote = True` default is True
5. Run test: `pytest -vv` or `pytest -vv -n 3` last one runs 3 parallels test