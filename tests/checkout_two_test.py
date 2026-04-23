from pages.inventory_page import InventoryPage
from test_data.login_data import get_sample_login_csv
from tests.base_test import BaseTest
from test_data.login_data import RegistrationDataGenerator


class CheckoutTwoTest(BaseTest):
    def setUp(self):
        super().setUp()
        login, password = get_sample_login_csv('test_data/login.csv')
        self.login_page.enter_username(login)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_random_products_to_cart()
        self.cart_page = self.inventory_page.click_shopping_cart_link()
        self.checkout_one_page = self.cart_page.click_checkout()
        self.data = RegistrationDataGenerator()
        self.checkout_one_page.enter_first_name(self.data.FIRST_NAME)
        self.checkout_one_page.enter_last_name(self.data.LAST_NAME)
        self.checkout_one_page.enter_postal_code(self.data.POSTAL_CODE)
        self.checkout_two_page = self.checkout_one_page.click_continue()

    def test_finish_checkout(self):
        self.checkout_two_page.click_finish_button()
        self.assertIn("checkout-complete", self.driver.current_url)