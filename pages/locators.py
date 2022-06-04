from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    #Log in field
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    LOGIN_BUTTON = (By.NAME, 'login_submit')

    #Register field
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_CONFIRM = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')