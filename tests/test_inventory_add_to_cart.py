import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.parametrize("driver", ["desktop", "mobile"], indirect=True)
def test_add_products_to_cart(logged_in_driver):
    """
    Verify cart badge count matches number of added products.
    """
    inventory_page = InventoryPage(logged_in_driver)

    items_added = inventory_page.add_products_to_cart(3)
    cart_count = inventory_page.get_cart_badge_text()

    print(f" Expected {items_added} items, got {cart_count}")
    assert cart_count == items_added
