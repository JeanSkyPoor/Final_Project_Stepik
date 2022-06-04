from pages.product_page import ProductPage
import time
import pytest
import json
from pages.locators import ProductPageLocators
from pages.locators import BasketPageLocators

with open('page_links.json') as f:
    data = json.load(f)['links']


@pytest.mark.parametrize('link', [pytest.param(data.pop(7), marks=pytest.mark.xfail), *data])
def test_guest_can_add_product_to_basket(browser, link) -> None:
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_item_name()
    page.check_item_price()
    

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser) -> None:
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


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser) -> None:
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    assert page.is_element_present(*BasketPageLocators.CONTINUE_BUY),\
        "Your basket is not empty"