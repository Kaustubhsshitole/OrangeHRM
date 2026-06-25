from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EntitlementsPage(BasePage):
    ENT_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Entitlements ')]")
    ADD_LINK = (By.XPATH, "//a[text()='Add Entitlements']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    ENT_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def add_entitlements(self, emp_name, count):
        self.click(self.ENT_DROPDOWN)
        self.click(self.ADD_LINK)
        self.write(self.EMPLOYEE_NAME_INPUT, emp_name)
        self.write(self.ENT_INPUT, count)
        self.click(self.SAVE_BUTTON)