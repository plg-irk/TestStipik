from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        print('self_out= ', self)

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print('self_url= ', self)
        print('self_url= ', self.url)
        assert "login" in self.url, "Login is not in url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print('self_form= ', self)
        self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        print('register_form= ', self)
        self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not"
        assert True