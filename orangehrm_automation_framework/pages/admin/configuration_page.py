from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ConfigurationPage(BasePage):
    CONFIG_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Configuration ')]")
    EMAIL_SUB_LINK = (By.XPATH, "//a[text()='Email Subscriptions']")
    EDIT_TOGGLE = (By.CSS_SELECTOR, "span.oxd-switch-input")

    def toggle_email_subscription(self):
        self.click(self.CONFIG_DROPDOWN)
        self.click(self.EMAIL_SUB_LINK)
        self.click(self.EDIT_TOGGLE)