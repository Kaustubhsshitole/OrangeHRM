from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyLeavePage(BasePage):
    MY_LEAVE_LINK = (By.XPATH, "//a[text()='My Leave']")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Show with Status']/ancestor::div[1]//div[@class='oxd-select-text-input']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def view_my_leave(self, status):
        self.click(self.MY_LEAVE_LINK)
        self.select_custom_dropdown_option(self.STATUS_DROPDOWN, status)
        self.click(self.SEARCH_BUTTON)