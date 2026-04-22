from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Locators:
    CART_REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_list > .cart_item button")
    CHECKOUT_BUTTON = (By.ID, "checkout")

class CartPage(BasePage):

    def remove_last_item(self):
        remove_buttons = self.driver.find_elements(*Locators.CART_REMOVE_BUTTONS)
        if len(remove_buttons) <= 1:
            print("There are no items to remove!")
            return
        remove_buttons[-1].click()