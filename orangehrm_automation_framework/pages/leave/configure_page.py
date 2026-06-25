from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeaveConfigurePage(BasePage):
    CONFIG_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Configure ')]")
    LEAVE_TYPES_LINK = (By.XPATH, "//a[text()='Leave Types']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    NAME_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def create_leave_type(self, name):
        self.click(self.CONFIG_DROPDOWN)
        self.click(self.LEAVE_TYPES_LINK)
        self.click(self.ADD_BUTTON)
        self.write(self.NAME_INPUT, name)
        self.click(self.SAVE_BUTTON)