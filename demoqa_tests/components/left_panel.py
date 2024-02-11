from selene import browser, have

class LeftPanel:

    def __init__(self):
        self.container = browser.element('.category-cards')
        self.menu = browser.element('.menu-list')

    def open(self, category, volume):
        browser.open('/')
        self.container.all('.card-body').element_by(have.text(category)).element("..").click()
        self.menu.all('.btn.btn-light').element_by(have.text(volume)).click()


    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')