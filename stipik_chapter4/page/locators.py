from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class PoductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT_OPTION = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_PRODUCT_OPTION_BASKET = (By.CSS_SELECTOR,
                                  "div.container-fluid.page > div > div > div:nth-child(1) > div > strong")
    PRICE_PRODUCT_OPTION = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRICE_PRODUCT_OPTION_BASKET = (By.CSS_SELECTOR,
                                "div.container-fluid.page > div > div > div:nth-child(3) > div> p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

