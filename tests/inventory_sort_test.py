from pages.inventory_page import InventoryPage
from test_data.login_data import get_sample_login_csv
from tests.conftest import BaseTest


class InventorySortTest(BaseTest):
    def setUp(self):
        super().setUp()
        login, password = get_sample_login_csv('test_data/login.csv')
        self.login_page.enter_username(login)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.inventory_page = InventoryPage(self.driver)

    def test_sort_by_name_az(self):
        self.inventory_page.click_sort_by_name_az()
        actual = self.inventory_page.get_product_names()
        expected = sorted(actual)
        self.assertEqual(actual, expected)

    def test_sort_by_name_za(self):
        self.inventory_page.click_sort_by_name_za()
        actual = self.inventory_page.get_product_names()
        expected = sorted(actual, reverse=True)
        self.assertEqual(actual, expected)

    def test_sort_by_price_asc(self):
        self.inventory_page.click_sort_by_price_asc()
        actual = self.inventory_page.get_product_prices()
        expected = sorted(actual)
        self.assertEqual(actual, expected)

    def test_sort_by_price_desc(self):
        self.inventory_page.click_sort_by_price_desc()
        actual = self.inventory_page.get_product_prices()
        expected = sorted(actual, reverse=True)
        self.assertEqual(actual, expected)