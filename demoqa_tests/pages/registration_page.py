from selene import browser, have, be
from selene.core import command
import allure
from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.all("[name=gender]")
        self.mobile = browser.element("#userNumber")
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

    @allure.step('Open main page')
    def open(self):
        browser.open("/automation-practice-form")
        # browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
        #     have.size_greater_than_or_equal(3))
        # browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)
        # browser.element('[aria-label="Consent"]').click()

    @allure.step('Input date of birth')
    def fill_date_of_birth(self, user: User):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").send_keys(user.date_of_birth_year)
        browser.element(".react-datepicker__month-select").send_keys(user.date_of_birth_month)
        browser.element(f".react-datepicker__day--0{user.date_of_birth_day}").click()

    @allure.step('Select hobbies')
    def select_hobbies(self, user: User):
        browser.element("[for=hobbies-checkbox-2]").perform(command.js.scroll_into_view)
        browser.all("[for=hobbies-checkbox-1]").element_by(have.exact_text(user.hobbies)).element("..").click()

    @allure.step('Select state')
    def fill_state(self, user: User):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.state)
        ).click()

    @allure.step('Select state')
    def fill_city(self, user: User):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.city)
        ).click()

    def registration(self, user: User):
        with allure.step('Input first name'):
            self.first_name.send_keys(user.first_name)
        with allure.step('Input last name'):
            self.last_name.send_keys(user.last_name)
        with allure.step('Input email'):
            self.email.send_keys(user.email)
        with allure.step('Select gender'):
            self.gender.element_by(have.value(user.gender)).element("..").click()
        with allure.step('Input phone number'):
            self.mobile.send_keys(user.phone_number)
        self.fill_date_of_birth(user)
        with allure.step('Type subjects'):
            self.subjects.type(user.subjects).press_enter()
        self.select_hobbies(user)
        with allure.step('Upload file'):
            self.picture.send_keys(resource.path(user.picture))
        with allure.step('Type current address'):
            self.current_address.send_keys(user.current_address)
        self.fill_state(user)
        self.fill_city(user)
        with allure.step('Press button submit form'):
            self.button_submit.submit()
        with allure.step('Close modal window'):
            self.button_modal.double_click()

    @allure.step('Checking registered user info')
    def should_have_registered_user_with(self, user: User):
        browser.element(".table").all("td:nth-child(2)").should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.phone_number,
                f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
                user.subjects,
                user.hobbies,
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )
