import pytest

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# @pytest.mark.parametrize(
#     'link', 
#     [
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#     ]
# )
def test_guest_can_add_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    book_title = page.get_book_title()
    book_price = page.get_book_price()

    page.should_be_added_message(book_title)
    page.should_basket_total_be_same_as_book_price(book_price)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()

#     assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES)


# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()

#     assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES)


# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()

#     assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES)
