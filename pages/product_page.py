from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(book_name)
        return book_name

    def should_be_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price
        # assert "£9.99" in price

    def basket_book_name(self):
        basket_book_name = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text
        print(basket_book_name)
        return basket_book_name

    def basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return basket_price

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        login_link.click()
