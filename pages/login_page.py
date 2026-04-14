from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    """
    Locators for elements on Login Page
    """
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_LINK = (By.ID, 'login-button')

class LoginPage(BasePage):
    """
    Login Page Object
    """
    def enter_username(self, username):
        """
        Enter username to login
        :param username:
        :return:
        """
        self.driver.find_element(*Locators.USERNAME).send_keys(username)

    def enter_password(self, password):
        """
        Enter password to login
        :param password:
        :return:
        """
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_login(self):
        """
        Click `login` button and goes to `inventory` page
        :return: InventoryPage Object
        """
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        return InventoryPage(self.driver)