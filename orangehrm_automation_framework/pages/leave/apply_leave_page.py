from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ApplyLeavePage(BasePage):
    APPLY_LINK = (By.XPATH, "//a[text()='Apply']")
    LEAVE_TYPE_DROPDOWN = (By.CSS_SELECTOR, "div.oxd-select-text")
    FROM_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    TO_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    COMMENT_BOX = (By.CSS_SELECTOR, "textarea.oxd-textarea")
    APPLY_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def apply_leave(self, l_type, f_date, t_date, comment):
        self.click(self.APPLY_LINK)
        self.select_custom_dropdown_option(self.LEAVE_TYPE_DROPDOWN, l_type)
        self.write(self.FROM_DATE, f_date)
        self.write(self.TO_DATE, t_date)
        self.write(self.COMMENT_BOX, comment)
        self.click(self.APPLY_BUTTON)