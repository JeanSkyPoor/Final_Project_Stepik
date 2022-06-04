from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        alert = self.browser.switch_to.alert
        alert.accept()

        
    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

