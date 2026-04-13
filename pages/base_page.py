class BasePage:
    """
    Base Page object for each page
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        """Site autotest"""
        return