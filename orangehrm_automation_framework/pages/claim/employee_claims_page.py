from selenium.webdriver.common.by import By
from pages.base_page import By, BasePage

class EmployeeClaimsPage(BasePage):
    EMP_CLAIMS_LINK = (By.XPATH, "//a[text()='Employee Claims']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def view_employee_claims(self):
        self.click(self.EMP_CLAIMS_LINK)
        self.click(self.SEARCH_BUTTON)