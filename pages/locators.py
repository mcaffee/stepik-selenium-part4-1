from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    LOGIN_LINK = MainPageLocators.LOGIN_LINK
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages > div.alert-success")
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')
    BOOK_TITLE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > span > a')
    ITEM_ROWS = (By.CSS_SELECTOR, '#basket_formset > div > div')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
