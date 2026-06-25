from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TimesheetsPage(BasePage):
    TIMESHEETS_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Timesheets ')]")
    MY_TS_LINK = (By.XPATH, "//a[text()='My Timesheets']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--ghost")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")

    def edit_and_submit_timesheet(self):
        self.click(self.TIMESHEETS_DROPDOWN)
        self.click(self.MY_TS_LINK)
        if self.is_visible(self.EDIT_BUTTON):
            self.click(self.EDIT_BUTTON)
            self.click(self.SUBMIT_BUTTON)