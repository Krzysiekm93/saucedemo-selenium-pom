from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Locators:
    """
    Inventory Page locators
    """
    SORT_CONTAINER = (By.CLASS_NAME, "select_container")
    SORT_BY_ITEM_NAME_AZ = (By.CSS_SELECTOR, '.product_sort_container option[value="az"]')
    SORT_BY_ITEM_NAME_ZA = (By.CSS_SELECTOR, '.product_sort_container option[value="za"]')
    SORT_BY_PRICE_DESC = (By.CSS_SELECTOR, '.product_sort_container option[value="lohi"]')
    SORT_BY_PRICE_ASC = (By.CSS_SELECTOR, '.product_sort_container option[value="hilo"]')


class InventoryPage(BasePage):
    """Inventory Page Object"""

    def _verify_page(self):
        """
        Verify the page is displayed
        """
        WebDriverWait(self.driver, 5).until(EC.url_matches("https://www.saucedemo.com/inventory.html"))

    def click_sort_by(self):
        self.driver.find_element(*Locators.SORT_CONTAINER).click()

    def click_sort_by_name_az(self):
        self.driver.find_element(*Locators.SORT_BY_ITEM_NAME_AZ).click()

    def click_sort_by_name_za(self):
        self.driver.find_element(*Locators.SORT_BY_ITEM_NAME_ZA).click()

    def click_sort_by_price_desc(self):
        self.driver.find_element(*Locators.SORT_BY_PRICE_DESC).click()

    def click_sort_by_price_asc(self):
        self.driver.find_element(*Locators.SORT_BY_PRICE_ASC).click()
