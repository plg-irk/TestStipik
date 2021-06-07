import pytest
from .page.main_page import MainPage
from .page.product_page import ProductPage
from .page.basket_page import BasketPage
from .page.login_page import LoginPage
import time
from .page.locators import PoductPageLocators
from .page.locators import BasePageLocators


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_register_form()
        users_email = str(time.time()) + "@fakemail.org"
        users_password = str(time.time()) + "password"
        self.login_page.register_new_user(users_email, users_password)
        self.login_page.should_be_authorized_user()
        self.page.open()

    def test_user_cant_see_success_message(self, browser):
        self.page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        self.page.checking_product_availability() # Проверяем присутствие товара и цену
        self.page.click_button_add_to_basket()  # Добавляем товар в корзину

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
                                  , "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                                 marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])

def test_guest_can_add_product_to_basket(browser,link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.checking_product_availability() # Проверяем присутствие товара и цену
    page.click_button_add_to_basket() # Добавляем товар в корзину
    page.solve_quiz_and_get_code() # Выполняем задание Stepik
    page.checking_exeption() # Проверяем ожидания

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.click_button_add_to_basket() # Добавляем товар в корзину
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.click_button_add_to_basket() # Добавляем товар в корзину
    page.disappeared_after_adding_product()

def test_guest_should_see_login_link_on_product_page(browser):
    # На странице товара есть ссылка на страницу регистрации для гостя
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    # Проверяем что гость переходит на страницу регистрации со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_product_is_not_in_basket_from_product_page(browser):
    # Проверяем что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()

@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page_negative(browser):
    # Проверяем появился или нет товар в корзине
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.product_is_not_in_empty_basket()







