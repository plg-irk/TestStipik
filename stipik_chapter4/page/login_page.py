from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # проверка на корректный url адрес
        print('self_url= ', self.url)
        assert "login" in self.url, "Login is not in url"
        assert True

    def should_be_login_form(self):
        # проверка что есть форма логина
        print('self_form= ', self.url)
        self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not"
        assert True

    def should_be_register_form(self):
        # проверка что есть форма регистрации на странице
        print('register_form= ', self.url)
        self.is_element_present(*BasePageLocators.REGISTER_FORM), "Register form is not"
        assert True

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        input_email.send_keys(email)

        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION)
        input_password1.send_keys(password)

        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION)
        input_password2.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button.click()


