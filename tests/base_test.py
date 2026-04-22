import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.login_page import LoginPage


class BaseTest(unittest.TestCase):
    """Base Test for each Test Case"""

    def setUp(self):
        #Initial preconditions
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()