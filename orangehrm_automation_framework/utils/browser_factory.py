from selenium import webdriver

class BrowserFactory:
    @staticmethod
    def create_driver(browser_name, headless=False):
        """Creates and returns a specific WebDriver with configured command line arguments."""
        b_name = browser_name.lower()
        if b_name == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Chrome(options=options)
            
        elif b_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            return webdriver.Firefox(options=options)
            
        elif b_name == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Edge(options=options)
            
        else:
            raise ValueError(f"Browser type '{browser_name}' is not supported by this framework.")