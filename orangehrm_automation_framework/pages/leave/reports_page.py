from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeaveReportsPage(BasePage):
    REPORTS_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Reports ')]")
    USAGE_REPORT_LINK = (By.XPATH, "//a[text()='Leave Entitlements and Usage Report']")
    GENERATE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def view_usage_reports(self):
        self.click(self.REPORTS_DROPDOWN)
        self.click(self.USAGE_REPORT_LINK)
        self.click(self.GENERATE_BUTTON)