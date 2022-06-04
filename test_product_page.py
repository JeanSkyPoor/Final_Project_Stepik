from pages.product_page import ProductPage
import pytest
import json
from pages.locators import  ProductPageLocators
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time

with open('page_links.json') as f:
    data = json.load(f)['links']



class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
       link = 'http://selenium1py.pythonanywhere.com/'
       page = MainPage(browser, link)
       page.open()
       page.go_to_login_page()
       login_page = LoginPage(browser, browser.current_url)
       login_page.register_new_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser) -> None:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_item_name()
        page.check_item_price()
        time.sleep(10)
    

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser) -> None:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser) -> None:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is not disappeared"


def test_guest_should_see_login_link_on_product_page(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser) -> None:
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    page = BasketPage(browser, browser.current_url)
    page.check_basket_is_empty()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser) -> None:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_item_name()
        page.check_item_price()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser) -> None:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()