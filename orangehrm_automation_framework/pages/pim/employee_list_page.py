from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EmployeeListPage(BasePage):
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/ancestor::div[1]//input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    TABLE_ROWS = (By.CSS_SELECTOR, ".oxd-table-card")
    DELETE_ICON = (By.CSS_SELECTOR, "i.oxd-icon.bi-trash")
    CONFIRM_DELETE = (By.CSS_SELECTOR, "button.oxd-button--label-danger")

    def search_employee(self, name):
        self.write(self.EMPLOYEE_NAME_INPUT, name)
        self.click(self.SEARCH_BUTTON)

    def delete_first_employee(self):
        self.click(self.DELETE_ICON)
        self.click(self.CONFIRM_DELETE)