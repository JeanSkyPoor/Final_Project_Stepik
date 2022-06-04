from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_BUY),\
            "Your basket is not empty"

    