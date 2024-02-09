import time

import allure
from selene import browser, have, be
from selene.core import command

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element("#firstName")  # .should(be.blank)
        self.last_name = browser.element("#lastName")  # .should(be.blank)
        self.email = browser.element("#userEmail")  # .should(be.blank)
        self.gender = browser.all("[name=gender]")
        self.mobile = browser.element("#userNumber")  # .should(be.blank)
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all("[type=checkbox]")
        self.picture = browser.element("#uploadPicture")
        self.current_address = browser.element("#currentAddress")
        self.submit = browser.element("#submit")
        self.subjects = browser.element('#subjectsInput')
        self.picture = browser.element("#uploadPicture")
        self.current_address = browser.element("#currentAddress")
        self.button_submit = browser.element("#submit")
        self.button_modal = browser.element("#closeLargeModal")

    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def fill_date_of_birth(self, user: User):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").send_keys(user.date_of_birth_year)
        browser.element(".react-datepicker__month-select").send_keys(user.date_of_birth_month)
        browser.element(f".react-datepicker__day--0{user.date_of_birth_day}").click()

    def select_hobbies(self, user: User):
        browser.element("[for=hobbies-checkbox-2]").perform(command.js.scroll_into_view)
        browser.all("[type=checkbox]").element_by(have.value(user.hobbies)).element("..").click()

    @allure.step('Checking registration form')
    def should_have_registered_user_with(
            self,
            first_name,
            last_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            state_city,
    ):
        browser.element(".table").all("td:nth-child(2)").should(
            have.exact_texts(
                f"{first_name} {last_name}",
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_city,
            )
        )

    def fill_state(self, user: User):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.state)
        ).click()

    def fill_city(self, user: User):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.city)
        ).click()

    @allure.step('Close modal window')
    def close_submiting_form(self):
        browser.element("#closeLargeModal").double_click()

    def registration(self, user: User):
        self.first_name.send_keys(user.first_name)
        self.last_name.send_keys(user.last_name)
        self.email.send_keys(user.email)
        self.gender.element_by(have.value(user.gender)).element("..").click()
        self.mobile.send_keys(user.phone_number)
        self.fill_date_of_birth(user)
        self.subjects.type(user.subjects).press_enter()
        self.select_hobbies(user)
        self.picture.send_keys(resource.path(user.picture))
        self.current_address.send_keys(user.current_address)

        self.fill_state(user)
        self.fill_city(user)
        time.sleep(3)
        self.button_submit.submit()
        self.button_modal.double_click()
