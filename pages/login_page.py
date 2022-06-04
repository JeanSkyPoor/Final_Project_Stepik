from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        assert 'login' in self.browser.current_url

    def should_be_login_form(self) -> None:
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
        

    def should_be_register_form(self) -> None:
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD)
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON)


    def register_new_user(self):

        self.email, self.password = BasePage.create_email_and_password(self)

        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(self.email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        BasePage.should_be_autorized_user(self)