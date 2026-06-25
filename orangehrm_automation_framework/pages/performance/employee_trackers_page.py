from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EmployeeTrackersPage(BasePage):
    EMP_TRACKERS_LINK = (By.XPATH, "//a[text()='Employee Trackers']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def search_employee_trackers(self):
        self.click(self.EMP_TRACKERS_LINK)
        self.click(self.SEARCH_BUTTON)