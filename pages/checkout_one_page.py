from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Locators:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

class CheckoutOnePage(BasePage):

    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*Locators.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*Locators.CONTINUE_BUTTON).click()