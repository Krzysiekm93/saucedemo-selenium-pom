from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class Locators:
    CART_REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_list > .cart_item button")
    CHECKOUT_BUTTON = (By.ID, "checkout")


class CartPage(BasePage):

    def remove_last_item(self):
        remove_buttons = self.driver.find_elements(*Locators.CART_REMOVE_BUTTONS)
        remove_buttons[-1].click()

    def click_checkout(self):
        self.driver.find_element(*Locators.CHECKOUT_BUTTON).click()
        return CheckoutPage(self.driver)
