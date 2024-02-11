from selene import browser, have, be
from selene.core import command

from demoqa_tests.data.users import User, SimpleUser


class SimpleUserRegistrationPage:

    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit_button = browser.element("#submit")

    def open(self):
        browser.open("/text-box")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def register(self, user: SimpleUser):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit_button.click()

    # def fill_full_name(self, value):
    #     self.full_name.type(value)
    #
    # def fill_email(self, value):
    #     self.email.type(value)
    #
    # def fill_current_address(self, value):
    #     self.current_address.type(value)
    #
    # def fill_permanent_address(self, value):
    #     self.permanent_address.type(value)
    #
    # def submit(self):
    #     self.submit_button.click()

# # создать папку степс и туда переложить
# class SimpleUserRegistrationSteps:
#
#     def __init__(self):
#         self.page = SimpleUserRegistrationPage()
#
#     # второй вариант
#     def register(self, user: User):
#         self.page.full_name.type(user.full_name)
#         self.page.email.type(user.email)
#         self.page.submit_button.submit()
#
#     def should_have_submited(self, full_name, email):
#         pass
