from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Locators:
    """
    Checkout Two-Page Object locators.
    """
    FINISH_BUTTON = (By.ID, 'finish')


class CheckoutTwoPage(BasePage):
    """
    Page Object for checkout step two (order overview) page.
    """

    def click_finish_button(self):
        """
        Click the `Finish` button to complete the checkout process.
        """
        self.wait_for_element_clickable(Locators.FINISH_BUTTON).click()
