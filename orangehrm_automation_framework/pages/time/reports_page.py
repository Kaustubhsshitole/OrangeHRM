from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TimeReportsPage(BasePage):
    REPORTS_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Reports ')]")
    PROJECT_REPORT = (By.XPATH, "//a[text()='Project Reports']")
    RUN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def run_project_report(self):
        self.click(self.REPORTS_DROPDOWN)
        self.click(self.PROJECT_REPORT)
        self.click(self.RUN_BUTTON)