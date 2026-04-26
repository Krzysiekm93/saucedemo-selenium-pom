import pytest
from pages.inventory_page import InventoryPage
from test_data.login_data import RegistrationDataGenerator


@pytest.mark.ui
@pytest.mark.parametrize("driver", ["desktop", "mobile"], indirect=True)
def test_checkout_information_continue(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_random_products_to_cart()
    cart_page = inventory_page.click_shopping_cart_link()
    checkout_one_page = cart_page.click_checkout()
    data = RegistrationDataGenerator()

    checkout_one_page.enter_first_name(data.FIRST_NAME)
    checkout_one_page.enter_last_name(data.LAST_NAME)
    checkout_one_page.enter_postal_code(data.POSTAL_CODE)
    checkout_one_page.click_continue()

    assert "checkout-step-two" in logged_in_driver.current_url
