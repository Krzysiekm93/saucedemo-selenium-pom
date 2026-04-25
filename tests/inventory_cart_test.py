from pages.inventory_page import InventoryPage
from test_data.login_data import get_sample_login_csv
from tests.conftest import BaseTest


class InventoryCartTest(BaseTest):
    def setUp(self):
        super().setUp()
        login, password = get_sample_login_csv('test_data/login.csv')
        self.login_page.enter_username(login)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.inventory_page = InventoryPage(self.driver)

    def test_add_products_to_cart(self):
        expected_count = self.inventory_page.add_random_products_to_cart()
        cart_count = self.inventory_page.get_cart_badge_text()
        print(f"Expected {expected_count}, got {cart_count}")
        assert cart_count == expected_count
