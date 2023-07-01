from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        self.url = self.browser.current_url
        assert 'login' in self.url, f'"url" haven`t word "login"'
        # реализуйте проверку на корректный url адрес
        # assert True

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "login form is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True