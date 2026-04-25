import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from test_data.login_data import get_sample_login_csv


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


def _create_driver(mobile: bool = False):
    if mobile:
        options = Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 12 Pro"})
        drv = webdriver.Chrome(options=options)
    else:
        drv = webdriver.Chrome()
        drv.maximize_window()
    return drv


@pytest.fixture
def driver(request, base_url):
    # default when used directly: desktop
    target = getattr(request, "param", "driver")

    if target == "driver":
        drv = _create_driver(mobile=False)
    elif target == "mobile_driver":
        drv = _create_driver(mobile=True)
    else:
        raise ValueError(f"Unsupported driver target: {target}")

    drv.get(base_url)
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def standard_user_credentials():
    username, password = get_sample_login_csv("test_data/login.csv")
    return {"username": username, "password": password}


def _login(driver, creds):
    login_page = LoginPage(driver)
    login_page.enter_username(creds["username"])
    login_page.enter_password(creds["password"])
    login_page.click_login()


@pytest.fixture
def logged_in_driver(driver, standard_user_credentials):
    _login(driver, standard_user_credentials)
    return driver


@pytest.fixture
def logged_in_mobile_driver(mobile_driver, standard_user_credentials):
    _login(mobile_driver, standard_user_credentials)
    return mobile_driver