from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base page object with shared browser driver access.
    """

    def __init__(self, driver):
        """
        Initialize the base page with a Selenium driver instance.
        """
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        """
        Site autotest.
        """
        return

    def wait_for_element(self, locator, timeout=10):
        """
        Wait for an element to be visible on the page.
        :param locator: A tuple containing the strategy and value (e.g., (By.ID, "username"))
        :param timeout: Maximum time to wait in seconds
        :return: The WebElement once it is visible
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Wait for an element to be clickable.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
