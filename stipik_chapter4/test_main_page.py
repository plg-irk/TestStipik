from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage
from .page.locators import BasePageLocators
import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_link_on_main_page(self, browser):
        #
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        #
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url) # инициализируем страницу
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()

def test_product_is_not_in_basket_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()

@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_main_page_negative(browser):
            # Проверяем появился или нет товар в корзине
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.product_is_not_in_empty_basket()
