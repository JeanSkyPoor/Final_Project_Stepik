from xmlrpc.client import Boolean
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators
import faker

class BasePage():
    def __init__(self, browser, url, timeout=10) -> None:
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)


    def open(self) -> None:
        self.browser.get(self.url)


    def is_element_present(self, how, what) -> Boolean:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def solve_quiz_and_get_code(self) -> None:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def is_not_element_present(self, how, what, timeout=4) -> Boolean:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False


    def is_disappeared(self, how, what, timeout=4) -> Boolean:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def go_to_login_page(self) -> None:
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()


    def should_be_login_link(self) -> None:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"


    def open_basket(self) -> None:
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()


    def create_email_and_password(self) -> list:
        self.f = faker.Faker()
        self.email = self.f.email()
        self.password = self.f.password()

        return [self.email, self.password]


    def should_be_autorized_user(self) -> None:
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
            "User icon is not presented"
