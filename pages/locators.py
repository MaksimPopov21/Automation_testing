from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    BOOK_NAME = (By.CSS_SELECTOR, '[class="active"]')
    PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, '[class="alertinner " ] strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"]')
    VIEW_BASKET = (By.CSS_SELECTOR, '[href="/en-gb/basket/"]')
