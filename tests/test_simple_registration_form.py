from demoqa_tests.application import app
from demoqa_tests.data import users
import allure
from allure_commons.types import Severity


@allure.tag('DemoQA')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'QAauto')
@allure.feature('Simple registration form')
@allure.story('Sent simple registration form')
@allure.link('https://demoqa.com', name='Text Box')
def test_registers_user():
    app.left_panel.open_simple_registration_form()
    app.simple_registration_form.register(users.semen)
    app.profile.should_have_submited_info(users.semen)
