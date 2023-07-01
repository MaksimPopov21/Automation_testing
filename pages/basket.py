from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage


class Basket(BasePage):

    def basket_book_name(self):
        basket_book_name = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text
        return basket_book_name

    def basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return basket_price

