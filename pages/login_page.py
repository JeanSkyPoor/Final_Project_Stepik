from distutils.log import Log
from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD)
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON)