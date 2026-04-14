from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Locators:
    """
    Inventory Page locators
    """

class InventoryPage(BasePage):
    """Inventory Page Object"""

    def _verify_page(self):
        """
        Verify the page is displayed
        """
        WebDriverWait(self.driver, 5).until(EC.url_matches("https://www.saucedemo.com/inventory.html"))