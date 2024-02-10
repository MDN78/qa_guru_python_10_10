import time

from demoqa_tests.data import users
from demoqa_tests.pages.simple_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()
    person = users.semen
    registration_page.open()
    registration_page.register(person)

    # registration_page.fill_full_name(person.full_name)
    # registration_page.fill_email(person.email)
    # registration_page.fill_current_address(person.current_address)
    # registration_page.fill_permanent_address(person.permanent_address)
    # # time.sleep(3)
    # registration_page.submit()
    registration_page.should_have_submited_info(person)
    time.sleep(3)
