import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.parametrize("driver", ["driver", "mobile_driver"], indirect=True)
def test_add_products_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    expected_count = inventory_page.add_random_products_to_cart()
    cart_count = inventory_page.get_cart_badge_text()

    print(f" Expected {expected_count} items, got {cart_count}")
    assert cart_count == expected_count