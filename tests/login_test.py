from ddt import ddt, data, unpack

import test_data.login_data
from pages.login_page import LoginPage
from tests.base_test import BaseTest

@ddt
class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)


    @data(*test_data.login_data.get_csv_data('test_data/login.csv'))
    @unpack
    def test_login_data(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()

