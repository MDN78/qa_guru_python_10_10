import allure
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver_configuration():
    with allure.step('Driver configuration'):
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options)

        browser.config.driver = driver
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.config.base_url = "https://demoqa.com"

    yield
    with allure.step('Close driver'):
        browser.quit()
