import random

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.cart_page import CartPage


class Locators:
    """
    Inventory Page Object locators.
    """
    SORT_CONTAINER = (By.CLASS_NAME, "select_container")
    SORT_BY_ITEM_NAME_AZ = (By.CSS_SELECTOR, '.product_sort_container option[value="az"]')
    SORT_BY_ITEM_NAME_ZA = (By.CSS_SELECTOR, '.product_sort_container option[value="za"]')
    SORT_BY_PRICE_ASC = (By.CSS_SELECTOR, '.product_sort_container option[value="lohi"]')
    SORT_BY_PRICE_DESC = (By.CSS_SELECTOR, '.product_sort_container option[value="hilo"]')
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price')
    BACKPACK_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    BIKE_LIGHT_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    BOLT_TSHIRT_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    FLEECE_JACKET_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
    ONESIE_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    RED_TSHIRT_ADD_TO_CART = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")


class InventoryPage(BasePage):
    """Inventory Page Object"""

    def _verify_page(self):
        """
        Verify the page is displayed
        """
        WebDriverWait(self.driver, 5).until(EC.url_matches("https://www.saucedemo.com/inventory.html"))

    def click_sort_by(self):
        """
        Click on inventory sort dropdown.
        """
        self.driver.find_element(*Locators.SORT_CONTAINER).click()

    def click_sort_by_name_az(self):
        """
        Select sorting by product name in ascending order (A to Z).
        """
        self.driver.find_element(*Locators.SORT_BY_ITEM_NAME_AZ).click()

    def click_sort_by_name_za(self):
        """"
        Select sorting by product name in descending order (Z to A).
        """
        self.driver.find_element(*Locators.SORT_BY_ITEM_NAME_ZA).click()

    def click_sort_by_price_desc(self):
        """
        Select sorting by price in descending order (high to low).
        """
        self.driver.find_element(*Locators.SORT_BY_PRICE_DESC).click()

    def click_sort_by_price_asc(self):
        """
        Select sorting by price in ascending order (low to high).
        """
        self.driver.find_element(*Locators.SORT_BY_PRICE_ASC).click()

    def get_product_names(self):
        """
        Return all visible product names in their current display order.
        """
        names = []
        items = self.driver.find_elements(*Locators.INVENTORY_ITEM_NAME)
        for item in items:
            names.append(item.text)
        return names

    def get_product_prices(self):
        """
        Return all visible product prices as floats in current display order.
        """
        prices = []
        items = self.driver.find_elements(*Locators.INVENTORY_ITEM_PRICE)
        for item in items:
            price = item.text.replace("$", "")
            prices.append(float(price))
        return prices

    def add_random_products_to_cart(self):
        """
        Add a random subset of products to the cart.
        """
        products = [
            Locators.BACKPACK_ADD_TO_CART,
            Locators.BIKE_LIGHT_ADD_TO_CART,
            Locators.BOLT_TSHIRT_ADD_TO_CART,
            Locators.FLEECE_JACKET_ADD_TO_CART,
            Locators.ONESIE_ADD_TO_CART,
            Locators.RED_TSHIRT_ADD_TO_CART,
        ]
        size = random.randint(1, 6)
        random_products = random.sample(products, size)

        for product in random_products:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(product)
            ).click()

        return size

    def get_cart_badge_text(self):
        """
        Get current cart badge quantity.
        """
        try:
            return int(self.driver.find_element(*Locators.QUANTITY).text)
        except NoSuchElementException:
            return 0

    def click_shopping_cart_link(self):
        """
        Open the shopping cart page.
        """
        self.driver.find_element(*Locators.SHOPPING_CART_LINK).click()
        return CartPage(self.driver)
