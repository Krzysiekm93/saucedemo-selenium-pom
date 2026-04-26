import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from test_data.login_data import get_sample_login_csv
from utils.devices import DEFAULT_MOBILE_DEVICE


def pytest_addoption(parser):
    parser.addoption(
        "--target",
        action="store",
        default="both",
        choices=["desktop", "mobile", "both"],
        help="Run tests for desktop, mobile, or both",
    )


def pytest_collection_modifyitems(config, items):
    target = config.getoption("--target")
    if target == "both":
        return

    selected = []
    deselected = []

    for item in items:
        callspec = getattr(item, "callspec", None)
        driver_target = None if callspec is None else callspec.params.get("driver")

        # Only filter parametrized tests that use the "driver" param
        if driver_target is None:
            selected.append(item)
            continue

        if target == "mobile" and driver_target == "mobile":
            selected.append(item)
        elif target == "desktop" and driver_target == "desktop":
            selected.append(item)
        else:
            deselected.append(item)

    items[:] = selected
    if deselected:
        config.hook.pytest_deselected(items=deselected)


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


def _create_driver(mobile: bool = False):
    if mobile:
        options = Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": DEFAULT_MOBILE_DEVICE})
        drv = webdriver.Chrome(options=options)
    else:
        drv = webdriver.Chrome()
        drv.maximize_window()
    return drv


@pytest.fixture
def driver(request, base_url):
    target = getattr(request, "param", "desktop")

    if target == "desktop":
        drv = _create_driver(mobile=False)
    elif target == "mobile":
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
