from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def check_basket_is_empty(self):
        assert "пуста" in self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY).text,\
            "Basket is empty or basket is not"

    def product_is_not_in_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_NOT_EMPTY), "Product is not in basket"
