from ddt import ddt, data, unpack
import test_data.login_data
from pages.login_page import LoginPage
from tests.conftest import BaseTest


@ddt
class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    @data(*[
        row for row in test_data.login_data.get_csv_data('test_data/login.csv')
        if row[0] != 'locked_out_user'
    ])
    @unpack
    def test_successful_login_data(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.assertIn('https://www.saucedemo.com/inventory.html', self.driver.current_url)

    @data(*[
        row for row in test_data.login_data.get_csv_data('test_data/login.csv')
        if row[0] == 'locked_out_user'
    ])
    @unpack
    def test_locked_out_login_data(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        expected_error_text = 'Epic sadface: Sorry, this user has been locked out.'
        actual_error_text = self.login_page.get_error()
        self.assertEqual(expected_error_text, actual_error_text)
