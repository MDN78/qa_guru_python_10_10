import pytest
from selene import browser, have, be
import time
from selene.core import command
from demoqa_tests import resource
from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name("Ivan")
    registration_page.fill_last_name("Ivanov")
    registration_page.fill_email("Ivanov@test.com")
    registration_page.select_gender("Male")
    registration_page.fill_phone_number("1234567890")
    registration_page.fill_date_of_birth("1980", "January", "10")
    registration_page.select_hobbies("1")
    registration_page.upload_picture("picture.jpg")
    registration_page.type_subjects('Physics')




    browser.element("#currentAddress").send_keys("111999, St Hall avenue 34")


    registration_page.fill_state("Haryana")

    registration_page.fill_city("Karnal")


    browser.element("#submit").submit()
    # THEN
    '''
    registration_page.registered_user_data.should(
        have.exact_texts(
                "Ivan Ivanov",
                "Ivanov@test.com",
                "Male",
                "1234567890",
                "10 January,1980",
                "Physics",
                "Sports",
                "picture.jpg",
                "111999, St Hall avenue 34",
                "Haryana Karnal",
        )
    )
    '''

    registration_page.should_have_registered_user_with(
        "Ivan",
        "Ivanov",
        "Ivanov@test.com",
        "Male",
        "1234567890",
        "10 January,1980",
        "Physics",
        "Sports",
        "picture.jpg",
        "111999, St Hall avenue 34",
        "Haryana Karnal",
    )

    browser.element("#closeLargeModal").double_click()

    time.sleep(4)
