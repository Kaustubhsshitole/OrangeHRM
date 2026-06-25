from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeaveListPage(BasePage):
    LEAVE_LIST_LINK = (By.XPATH, "//a[text()='Leave List']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    APPROVE_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")

    def approve_first_leave(self):
        self.click(self.LEAVE_LIST_LINK)
        self.click(self.SEARCH_BUTTON)
        if self.is_visible(self.APPROVE_BUTTON):
            self.click(self.APPROVE_BUTTON)