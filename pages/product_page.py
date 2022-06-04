from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self) -> None:
        self.is_element_present(*ProductPageLocators.BASKET_BUTTON)
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()


    def check_item_name(self) -> None:
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert item_name == added_item_name, 'Name is different'


    def check_item_price(self) -> None:
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text[1:]
        added_item_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert item_price == added_item_price, 'Price is different'


    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should bot be"

    def check_success_message_is_not_present(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def check_success_message_is_disappeared(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is not disappeared"