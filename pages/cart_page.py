from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_one_page import CheckoutOnePage


class Locators:
    CART_REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_list > .cart_item button")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")


class CartPage(BasePage):

    def remove_last_item(self):
        remove_buttons = self.driver.find_elements(*Locators.CART_REMOVE_BUTTONS)
        remove_buttons[-1].click()

    def click_checkout(self):
        self.driver.find_element(*Locators.CHECKOUT_BUTTON).click()
        return CheckoutOnePage(self.driver)

    def get_cart_item_names(self):
        return [el.text.strip() for el in self.driver.find_elements(*Locators.CART_ITEM_NAMES)]
