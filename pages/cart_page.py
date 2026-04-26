from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_one_page import CheckoutOnePage


class Locators:
    """
    Cart Page Object Locators.
    """
    CART_REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_list > .cart_item button")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")


class CartPage(BasePage):
    """
    Page Object for interactions available on the shopping cart page.
    """

    def remove_last_item(self):
        """
        Remove the last product currently listed in the cart.
        """
        remove_buttons = self.driver.find_elements(*Locators.CART_REMOVE_BUTTONS)
        remove_buttons[-1].click()

    def click_checkout(self):
        """
        Proceed from cart to checkout step one.
        """
        self.driver.find_element(*Locators.CHECKOUT_BUTTON).click()
        return CheckoutOnePage(self.driver)

    def get_cart_item_names(self):
        """
        Get names of all items currently displayed in the cart.
        """
        return [el.text.strip() for el in self.driver.find_elements(*Locators.CART_ITEM_NAMES)]
