from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ManageReviewsPage(BasePage):
    MANAGE_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Manage Reviews ')]")
    ASSIGN_LINK = (By.XPATH, "//a[text()='Assign Reviews']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def assign_review(self):
        self.click(self.MANAGE_DROPDOWN)
        self.click(self.ASSIGN_LINK)
        self.click(self.SAVE_BUTTON)