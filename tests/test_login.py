import pytest
import test_data.login_data
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.parametrize("driver", ["driver", "mobile_driver"], indirect=True)
@pytest.mark.parametrize(
    "username,password",
    [
        row for row in test_data.login_data.get_csv_data("test_data/login.csv")
        if row[0] != "locked_out_user"
    ],
)
def test_successful_login_data(driver, username, password):
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url


@pytest.mark.ui
@pytest.mark.parametrize("driver", ["driver", "mobile_driver"], indirect=True)
@pytest.mark.parametrize(
    "username,password",
    [
        row for row in test_data.login_data.get_csv_data("test_data/login.csv")
        if row[0] == "locked_out_user"
    ],
)
def test_locked_out_login_data(driver, username, password):
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    expected_error_text = "Epic sadface: Sorry, this user has been locked out."
    actual_error_text = login_page.get_error()
    assert expected_error_text == actual_error_text
