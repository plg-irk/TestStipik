from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):

    def click_button_add_to_basket(self):
        button_add_backet = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        button_add_backet.click()

    def name_product_option(self):
        name_product = self.browser.find_element(*MainPageLocators.NAME_PRODUCT_OPTION)
        return name_product

    def name_product_option_basket(self):
        name_product_basket = self.browser.find_element(*MainPageLocators.NAME_PRODUCT_OPTION_BASKET)
        return name_product_basket

    def prices_product_option(self):
        prices_product = self.browser.find_element(*MainPageLocators.PRICE_PRODUCT_OPTION)
        return prices_product

    def prices_product_option_basket(self):
        prices_product_basket = self.browser.find_element(*MainPageLocators.PRICE_PRODUCT_OPTION_BASKET)
        return prices_product_basket

