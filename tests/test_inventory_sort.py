import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_sort_by_name_az(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.click_sort_by_name_az()
    actual = inventory_page.get_product_names()
    expected = sorted(actual)
    assert actual == expected


@pytest.mark.ui
def test_sort_by_name_za(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.click_sort_by_name_za()
    actual = inventory_page.get_product_names()
    expected = sorted(actual, reverse=True)
    assert actual == expected


@pytest.mark.ui
def test_sort_by_price_asc(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.click_sort_by_price_asc()
    actual = inventory_page.get_product_prices()
    expected = sorted(actual)
    assert actual == expected


@pytest.mark.ui
def test_sort_by_price_desc(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.click_sort_by_price_desc()
    actual = inventory_page.get_product_prices()
    expected = sorted(actual, reverse=True)
    assert actual == expected