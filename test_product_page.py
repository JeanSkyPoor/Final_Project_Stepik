from pages.product_page import ProductPage
import time
import pytest
import json

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
    