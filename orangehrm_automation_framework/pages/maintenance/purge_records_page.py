from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PurgeRecordsPage(BasePage):
    PWD_POPUP_INPUT = (By.XPATH, "//input[@type='password']")
    CONFIRM_PWD_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PURGE_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Purge Records ')]")
    CANDIDATES_LINK = (By.XPATH, "//a[text()='Vacant Candidate Records']")

    def unlock_maintenance(self, password):
        """Passes administrative password challenge to access Maintenance module."""
        if self.is_visible(self.PWD_POPUP_INPUT):
            self.write(self.PWD_POPUP_INPUT, password)
            self.click(self.CONFIRM_PWD_BUTTON)

    def purge_records(self):
        self.click(self.PURGE_DROPDOWN)
        self.click(self.CANDIDATES_LINK)