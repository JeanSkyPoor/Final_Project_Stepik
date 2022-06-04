from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self) -> None:
        self.is_element_present(*ProductPageLocators.BASKET_BUTTON)
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()