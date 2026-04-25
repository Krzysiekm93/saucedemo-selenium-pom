import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


@pytest.fixture
def driver(base_url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture
def standard_user_credentials():
    return {"username": "standard_user", "password": "secret_sauce"}


@pytest.fixture
def logged_in_driver(driver, standard_user_credentials):
    login_page = LoginPage(driver)
    login_page.enter_username(standard_user_credentials["username"])
    login_page.enter_password(standard_user_credentials["password"])
    login_page.click_login()
    return driver