from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddEmployeePage(BasePage):
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    EMPLOYEE_ID = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_DETAILS_TOGGLE = (By.CSS_SELECTOR, "span.oxd-switch-input")
    
    USERNAME_FIELD = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
    PASSWORD_FIELD = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")

    def add_employee(self, fname, mname, lname, empid):
        self.write(self.FIRST_NAME, fname)
        self.write(self.MIDDLE_NAME, mname)
        self.write(self.LAST_NAME, lname)
        if empid:
            self.write(self.EMPLOYEE_ID, empid)
        self.click(self.SAVE_BUTTON)

    def add_employee_with_credentials(self, fname, lname, uname, pwd):
        self.write(self.FIRST_NAME, fname)
        self.write(self.LAST_NAME, lname)
        self.click(self.LOGIN_DETAILS_TOGGLE)
        self.write(self.USERNAME_FIELD, uname)
        self.write(self.PASSWORD_FIELD, pwd)
        self.write(self.CONFIRM_PASSWORD, pwd)
        self.click(self.SAVE_BUTTON)