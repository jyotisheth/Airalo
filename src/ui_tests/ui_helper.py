from selenium import webdriver
import json

class Config:
    def __init__(self):
        self.config = json.loads(open("../config.json").read())

    def base_url(self):
        return self.config["default"]["UI_BASE_URL"]

class ChromeDriver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("test-type=browser")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("-incognito")
        self.options.add_argument("--disable-notification")
        self.options.add_argument("--disable-cookies")
        self.driver = webdriver.Chrome(self.options)

    def chrome(self):
        return self.driver

class UiElements:
    btn_accept_cookies = "[id=onetrust-accept-btn-handler]"
    btn_no_allow_push = "[id=wzrk-cancel]"
    textbox_search = "[data-testid=search-input]"
    list_value_Japan = "[data-testid=Japan-name]"
    list_eSIM_plans = "[data-testid=esim-button]"
    popup_eSIM_plan = "[data-testid=sim-detail-header]"
    element_package_title = "[data-testid=sim-detail-operator-title]"
    element_package_coverage = "[data-testid=COVERAGE-value]"
    element_package_data = "[data-testid=DATA-value]"
    element_package_validity = "[data-testid=VALIDITY-value]"
    element_package_price = "[data-testid=PRICE-value]"