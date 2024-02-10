from demoqa_tests.data import users
from demoqa_tests.pages.simple_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()
    admin = users.semen
    registration_page.open()
    registration_page.fill_full_name(admin.full_name)
    registration_page.fill_email(admin.email)
    registration_page.submit()