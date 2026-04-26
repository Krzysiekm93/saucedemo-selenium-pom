from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_two_page import CheckoutTwoPage


class Locators:
    """
    Checkout One-Page Object locators.
    """
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

class CheckoutOnePage(BasePage):
    """Page Object for checkout step one (customer information) page."""
    def enter_first_name(self, first_name):
        """
        Enter customer `first name` into the checkout form.
        """
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enter customer `last name` into the checkout form.
        """
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """
        Enter customer postal code into the checkout form.
        """
        self.driver.find_element(*Locators.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        """
        Submit checkout information and go to checkout step two.
        """
        self.driver.find_element(*Locators.CONTINUE_BUTTON).click()
        return CheckoutTwoPage(self.driver)