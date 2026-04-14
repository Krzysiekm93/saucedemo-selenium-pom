from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    """
    Locators for elements on Login Page
    """
    LOGIN_LINK = (By.ID, 'login-button')

class LoginPage(BasePage):
    """
    Login Page Object
    """
    def click_login(self):
        """
        Click `login` button and goes to `inventory` page
        :return: InventoryPage Object
        """
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        return InventoryPage(self.driver)