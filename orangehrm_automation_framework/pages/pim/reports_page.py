from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMReportsPage(BasePage):
    REPORTS_LINK = (By.XPATH, "//a[text()='Reports']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def run_report(self, title):
        self.click(self.REPORTS_LINK)
        self.write(self.SEARCH_INPUT, title)
        self.click(self.SEARCH_BUTTON)