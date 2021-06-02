from .base_page import BasePage
from .locators import PoductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):

    def checking_product_availability(self):
        self.is_element_present(*PoductPageLocators.NAME_PRODUCT_OPTION)
        self.is_element_present(*PoductPageLocators.PRICE_PRODUCT_OPTION)

    def click_button_add_to_basket(self):
        button_add_backet = self.browser.find_element(*PoductPageLocators.ADD_TO_BASKET)
        button_add_backet.click()

    def name_product_option(self):
        name_product = self.browser.find_element(*PoductPageLocators.NAME_PRODUCT_OPTION)
        return name_product

    def name_product_option_basket(self):
        name_product_basket = self.browser.find_element(*PoductPageLocators.NAME_PRODUCT_OPTION_BASKET)
        return name_product_basket

    def prices_product_option(self):
        prices_product = self.browser.find_element(*PoductPageLocators.PRICE_PRODUCT_OPTION)
        return prices_product

    def prices_product_option_basket(self):
        prices_product_basket = self.browser.find_element(*PoductPageLocators.PRICE_PRODUCT_OPTION_BASKET)
        return prices_product_basket

    def checking_exeption(self):
        assert self.name_product_option_basket().text == self.name_product_option().text,\
            "Product is not option"
                # Проверяем выбор товара и цену
        assert self.prices_product_option_basket().text == self.prices_product_option().text,\
            "Price is not equal"

    def checking_do_not_message_add_product(self):
        self.checking_do_not_message_add_product(*PoductPageLocators.NAME_PRODUCT_OPTION_BASKET)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PoductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



