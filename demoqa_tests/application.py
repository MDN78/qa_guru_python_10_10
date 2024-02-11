from demoqa_tests.pages.profile_page import ProfilePage
from demoqa_tests.pages.simple_registration_page import SimpleUserRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_registration_form = SimpleUserRegistrationPage()
        self.profile = ProfilePage()


app = ApplicationManager()
