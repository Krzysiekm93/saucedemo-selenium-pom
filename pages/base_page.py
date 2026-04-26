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
