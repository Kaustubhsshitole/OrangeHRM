from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AssignLeavePage(BasePage):
    ASSIGN_LINK = (By.XPATH, "//a[text()='Assign Leave']")
    EMP_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    LEAVE_TYPE_DROPDOWN = (By.CSS_SELECTOR, "div.oxd-select-text")
    FROM_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    ASSIGN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def assign_leave_to_employee(self, emp, ltype, date):
        self.click(self.ASSIGN_LINK)
        self.write(self.EMP_NAME_INPUT, emp)
        self.select_custom_dropdown_option(self.LEAVE_TYPE_DROPDOWN, ltype)
        self.write(self.FROM_DATE, date)
        self.click(self.ASSIGN_BUTTON)