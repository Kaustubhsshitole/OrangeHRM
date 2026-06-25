from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyTrackersPage(BasePage):
    MY_TRACKERS_LINK = (By.XPATH, "//a[text()='My Trackers']")
    TRACKER_LOGS = (By.CSS_SELECTOR, "div.orangehrm-tracker-log")

    def count_tracker_logs(self):
        self.click(self.MY_TRACKERS_LINK)
        return len(self.driver.find_elements(*self.TRACKER_LOGS))