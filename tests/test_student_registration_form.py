import pytest
from allure_commons.types import Severity
from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage
import allure


@allure.tag('DemoQA')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'QAauto')
@allure.feature('Student Registration Form')
@allure.story('Sent registration form')
@allure.link('https://demoqa.com', name='Practice Form')
def test_student_registration_form_2():
    registration_page = RegistrationPage()
    student = users.oleg
    registration_page.open()
    # WHEN
    registration_page.registration(student)
    # THEN
    registration_page.should_have_registered_user_with(student)
