import allure
import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def driver_configuration():
    with allure.step('Driver configuration'):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.config.base_url = "https://demoqa.com"

    yield
    with allure.step('Close driver'):
        browser.quit()
