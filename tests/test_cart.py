import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_remove_last_item(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_random_products_to_cart()
    cart_page = inventory_page.click_shopping_cart_link()

    items_before = cart_page.get_cart_item_names()
    last_item_before = items_before[-1]

    cart_count_before_remove = int(inventory_page.get_cart_badge_text())
    cart_page.remove_last_item()

    items_after = cart_page.get_cart_item_names()
    cart_count_after_remove = int(inventory_page.get_cart_badge_text())

    print(f" Before: {cart_count_before_remove}, after: {cart_count_after_remove}, removed last item: {last_item_before}")
    assert cart_count_after_remove == cart_count_before_remove - 1
    assert last_item_before not in items_after, f"Expected removed last item '{last_item_before}' to be absent"
