import allure
from selene import browser, have
from selene.core import command

from demoqa_tests.data.users import SimpleUser


class SimpleUserRegistrationPage:

    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit_button = browser.element("#submit")

    @allure.step('Open main page')
    def open(self):
        browser.open("/text-box")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def register(self, user: SimpleUser):
        with allure.step('Fill full name'):
            self.full_name.type(user.full_name)
        with allure.step('Fill email'):
            self.email.type(user.email)
        with allure.step('Type current address'):
            self.current_address.type(user.current_address)
        with allure.step('Type permanent address'):
            self.permanent_address.type(user.permanent_address)
        browser.element('#submit').perform(command.js.scroll_into_view)
        with allure.step('Submit form'):
            self.submit_button.click()
