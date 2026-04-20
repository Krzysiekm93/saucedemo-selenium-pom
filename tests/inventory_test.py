from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class InventoryTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
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

