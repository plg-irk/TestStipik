from .base_page import BasePage
from .locators import PoductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):

    def checking_product_availability(self):
        # Проверка присутствия товара и цены
        self.is_element_present(*PoductPageLocators.NAME_PRODUCT_OPTION)
        self.is_element_present(*PoductPageLocators.PRICE_PRODUCT_OPTION)

    def click_button_add_to_basket(self):
        # Добавление товара в корзину
        button_add_backet = self.browser.find_element(*PoductPageLocators.ADD_TO_BASKET)
        button_add_backet.click()

    def name_product_option(self):
        # Наименование товара
        name_product = self.browser.find_element(*PoductPageLocators.NAME_PRODUCT_OPTION)
        return name_product

    def name_product_option_basket(self):
        # Наименование товара в корзине
        name_product_basket = self.browser.find_element(*PoductPageLocators.NAME_PRODUCT_OPTION_BASKET)
        return name_product_basket

    def prices_product_option(self):
        # Цена товара
        prices_product = self.browser.find_element(*PoductPageLocators.PRICE_PRODUCT_OPTION)
        return prices_product

    def prices_product_option_basket(self):
        # Цена товара в корзине
        prices_product_basket = self.browser.find_element(*PoductPageLocators.PRICE_PRODUCT_OPTION_BASKET)
        return prices_product_basket

    def checking_exeption(self):
        # Проверяем выбор товара и цену
        assert self.name_product_option_basket().text == self.name_product_option().text,\
            "Product is not option"
        assert self.prices_product_option_basket().text == self.prices_product_option().text,\
            "Price is not equal"

    def checking_do_not_message_add_product(self):
        # Проверяем отсутствие товара в корзине
        self.checking_do_not_message_add_product(*PoductPageLocators.NAME_PRODUCT_OPTION_BASKET)

    def should_not_be_success_message(self):
        #
        assert self.is_not_element_present(*PoductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def disappeared_after_adding_product(self):
        assert self.is_disappeared(*PoductPageLocators.SUCCESS_MESSAGE)



