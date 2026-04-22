import time

from test_data.login_data import get_sample_login_csv
from tests.base_test import BaseTest


class CartTest(BaseTest):
    def setUp(self):
        super().setUp()
        login, password = get_sample_login_csv('test_data/login.csv')
        self.login_page.enter_username(login)
        self.login_page.enter_password(password)
        self.inventory_page = self.login_page.click_login()
        self.inventory_page.add_random_products_to_cart()
        self.cart_page = self.inventory_page.click_shopping_cart_link()

    def test_remove_last_item(self):
        cart_count_before_remove = int(self.inventory_page.get_cart_badge_text())
        self.cart_page.remove_last_item()
        cart_count_after_remove = int(self.inventory_page.get_cart_badge_text())
        print(f"Before: {cart_count_before_remove}, after: {cart_count_after_remove}")
        assert cart_count_after_remove == cart_count_before_remove - 1
