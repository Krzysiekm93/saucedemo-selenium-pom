import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from test_data.login_data import get_sample_login_csv


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


@pytest.fixture(scope="session")
def standard_user_credentials():
    username, password = get_sample_login_csv("test_data/login.csv")
    return {"username": username, "password": password}


@pytest.fixture
def logged_in_driver(driver, standard_user_credentials):
    login_page = LoginPage(driver)
    login_page.enter_username(standard_user_credentials["username"])
    login_page.enter_password(standard_user_credentials["password"])
    login_page.click_login()
    return driver