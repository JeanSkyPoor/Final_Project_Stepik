from multiprocessing.connection import wait
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser) -> None:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    while True:
        time.sleep(1)