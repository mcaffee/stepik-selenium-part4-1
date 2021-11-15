from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        return book_title.text

    def get_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def is_message_present(self, text):
        all_messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        for m in all_messages:
            if text in m.text:
                return True
        return False

    def should_be_added_message(self, book_title):
        assert self.is_message_present(f'{book_title} has been added to your basket.')

    def should_basket_total_be_same_as_book_price(self, book_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert f'Basket total: {book_price}' in basket_total.text
