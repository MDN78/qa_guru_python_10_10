from demoqa_tests.application import app
from demoqa_tests.data import users
from demoqa_tests.pages.profile_page import ProfilePage
from demoqa_tests.pages.simple_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    # app.simple_registration_form.open()
    app.left_panel.open_simple_registration_form()
    app.simple_registration_form.register(users.semen)
    app.profile.should_have_submited_info(users.semen)

    # time.sleep(3)

    # simple_registration_form = SimpleUserRegistrationPage()
    # profile_page = ProfilePage()
    # person = users.semen
    # simple_registration_form.register(person)
    # registration_page.fill_full_name(person.full_name)
    # registration_page.fill_email(person.email)
    # registration_page.fill_current_address(person.current_address)
    # registration_page.fill_permanent_address(person.permanent_address)
    # # time.sleep(3)
    # registration_page.submit()
