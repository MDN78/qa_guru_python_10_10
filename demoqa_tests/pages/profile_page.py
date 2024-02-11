from demoqa_tests.data.users import SimpleUser
from selene import browser, have


class ProfilePage:

    def should_have_submited_info(self, user: SimpleUser):
        browser.element('.border').all('p').should(
            have.exact_texts(
                f'Name:{user.full_name}',
                f'Email:{user.email}',
                f'Current Address :{user.current_address}',
                f'Permananet Address :{user.permanent_address}',
            )
        )
