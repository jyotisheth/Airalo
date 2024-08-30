from ui_helper import Config, UiElements, ChromeDriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_airalo_japan_pkg():
    ### Variables ###

    country_name = "Japan"
    package_title = "Moshi Moshi"
    package_coverage = "Japan"
    package_data = "1 GB"
    package_validity = "7 Days"
    package_price = "4.50 €"

    ### 1. Launch Airalo website
    driver = ChromeDriver().chrome()
    driver.get("https://www.airalo.com/")
    time.sleep(5)
    accept_cookies_element = driver.find_element(By.CSS_SELECTOR, UiElements.btn_accept_cookies)
    accept_cookies_element.click()
    time.sleep(2)
    no_allow_push_element = driver.find_element(By.CSS_SELECTOR, UiElements.btn_no_allow_push)
    no_allow_push_element.click()

    ### 2. Search for Japan
    search_box = driver.find_element(By.CSS_SELECTOR, UiElements.textbox_search)
    search_box.send_keys(country_name)
    time.sleep(5)
    japan_local_element = driver.find_element(By.CSS_SELECTOR, UiElements.list_value_Japan)
    japan_local_element.click()
    time.sleep(5)

    ### 3. Select an eSIM package
    elements = driver.find_elements(By.CSS_SELECTOR, UiElements.list_eSIM_plans)
    elements[0].click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, UiElements.popup_eSIM_plan)

    ### 4. Verify package details
    japan_package_title = driver.find_element(By.CSS_SELECTOR, UiElements.element_package_title).text
    #print("Title:{0}".format(japan_package_title))
    assert japan_package_title == package_title, "Package details: title did not match"
    japan_package_coverage = driver.find_element(By.CSS_SELECTOR, UiElements.element_package_coverage).text
    #print("Coverage:{0}".format(japan_package_coverage))
    assert japan_package_coverage == package_coverage, "Package details: Coverage did not match"
    japan_package_data = driver.find_element(By.CSS_SELECTOR, UiElements.element_package_data).text
    #print("Data:{0}".format(japan_package_data))
    assert japan_package_data == package_data, "Package details: Data did not match"
    japan_package_validity = driver.find_element(By.CSS_SELECTOR, UiElements.element_package_validity).text
    #print("Validity:{0}".format(japan_package_validity))
    assert japan_package_validity == package_validity, "Package details: Validity did not match"
    japan_package_price = driver.find_element(By.CSS_SELECTOR, UiElements.element_package_price).text
    #print("Price:{0}".format(japan_package_price))
    assert japan_package_price == package_price, (
        "Package details: Price did not match, expected {} found{}".format(package_price, japan_package_price))
    print("Airalo-Japan-eSIM package details : verified")