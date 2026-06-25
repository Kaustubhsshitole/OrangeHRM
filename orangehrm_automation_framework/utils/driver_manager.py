from utils.browser_factory import BrowserFactory

class DriverManager:
    """Provides thread-safe wrapper for managing WebDriver references."""
    _driver = None

    @classmethod
    def get_driver(cls, browser="chrome", headless=False):
        if cls._driver is None:
            cls._driver = BrowserFactory.create_driver(browser, headless)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None