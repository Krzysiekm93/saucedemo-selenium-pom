from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Locators:
    FINISH_BUTTON = (By.ID, 'finish')

class CheckoutTwoPage(BasePage):

    def click_finish_button(self):
        self.driver.find_element(*Locators.FINISH_BUTTON)