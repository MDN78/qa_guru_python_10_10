from selene import browser, have
import allure


class LeftPanel:

    def __init__(self):
        self.container = browser.element('.category-cards')
        self.menu = browser.element('.menu-list')

    @allure.step('Open category {category} and menu {volume}')
    def open(self, category, volume):
        browser.open('/')
        self.container.all('.card-body').element_by(have.text(category)).element("..").click()
        self.menu.all('.btn.btn-light').element_by(have.text(volume)).click()

    @allure.step('Open simple registration panel via left menu')
    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
