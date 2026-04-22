from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class InventoryCartTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()
        self.inventory_page = InventoryPage(self.driver)

    def test_add_products_to_cart(self):
        expected_count = self.inventory_page.add_random_products_to_cart()
        cart_count = self.inventory_page.get_cart_badge_text()
        print(f"Expected {expected_count}, got {cart_count}")
        assert cart_count == expected_count
