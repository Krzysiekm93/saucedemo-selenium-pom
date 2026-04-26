import pytest
from pages.inventory_page import InventoryPage
from test_data.login_data import RegistrationDataGenerator


@pytest.mark.ui
@pytest.mark.parametrize("driver", ["desktop", "mobile"], indirect=True)
def test_finish_checkout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_random_products_to_cart()
    cart_page = inventory_page.click_shopping_cart_link()
    checkout_one_page = cart_page.click_checkout()

    data = RegistrationDataGenerator()
    checkout_one_page.enter_first_name(data.FIRST_NAME)
    checkout_one_page.enter_last_name(data.LAST_NAME)
    checkout_one_page.enter_postal_code(data.POSTAL_CODE)

    checkout_two_page = checkout_one_page.click_continue()
    checkout_two_page.click_finish_button()

    assert "checkout-complete" in logged_in_driver.current_url