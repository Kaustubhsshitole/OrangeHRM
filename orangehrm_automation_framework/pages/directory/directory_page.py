from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DirectoryPage(BasePage):
    SEARCH_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def filter_directory(self, name):
        self.write(self.SEARCH_NAME, name)
        self.click(self.SEARCH_BUTTON)