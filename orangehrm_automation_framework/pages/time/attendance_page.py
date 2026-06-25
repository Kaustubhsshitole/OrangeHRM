from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AttendancePage(BasePage):
    ATT_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Attendance ')]")
    PUNCH_LINK = (By.XPATH, "//a[text()='Punch In/Out']")
    NOTE_TEXTAREA = (By.CSS_SELECTOR, "textarea.oxd-textarea")
    PUNCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def punch_in_out(self, note):
        self.click(self.ATT_DROPDOWN)
        self.click(self.PUNCH_LINK)
        self.write(self.NOTE_TEXTAREA, note)
        self.click(self.PUNCH_BUTTON)