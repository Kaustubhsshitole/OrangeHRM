from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AssignClaimsPage(BasePage):
    ASSIGN_LINK = (By.XPATH, "//a[text()='Assign Claim']")
    EMP_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def assign_claim(self, name):
        self.click(self.ASSIGN_LINK)
        self.write(self.EMP_NAME_INPUT, name)
        self.click(self.SAVE_BUTTON)