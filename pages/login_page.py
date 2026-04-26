from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    """
    Locators for elements on Login Page Object.
    """
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_LINK = (By.ID, 'login-button')
    VISIBLE_ERROR = (By.CLASS_NAME, "error-message-container.error")


class LoginPage(BasePage):
    """
    Page object for SauceDemo login screen.
    """

    def enter_username(self, username):
        """
        Enter `username` to login.
        """
        self.driver.find_element(*Locators.USERNAME).send_keys(username)

    def enter_password(self, password):
        """
        Enter `password` to login.
        """
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_login(self):
        """
        Click the `login` button to submit credentials.
        """
        self.driver.find_element(*Locators.LOGIN_LINK).click()

    def get_error(self):
        """
        Return error message.
        """
        return self.driver.find_element(*Locators.VISIBLE_ERROR).text
