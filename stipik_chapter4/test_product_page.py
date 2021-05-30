from .page.product_page import ProductPage
import time
from .page.locators import MainPageLocators

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу

    page.click_button_add_to_basket() # Добавляем товар в корзину

    page.solve_quiz_and_get_code() # Выполняем задание Stepik

    assert page.name_product_option_basket().text == page.name_product_option().text,\
        "Product is not option"
            # Проверяем ожидания
    assert page.prices_product_option_basket().text == page.prices_product_option().text,\
        "Price is not equal"
