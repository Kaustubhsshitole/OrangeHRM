from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMConfigurationPage(BasePage):
    CONFIG_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Configuration ')]")
    OPTIONAL_FIELDS_LINK = (By.XPATH, "//a[text()='Optional Fields']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def save_pim_config(self):
        self.click(self.CONFIG_DROPDOWN)
        self.click(self.OPTIONAL_FIELDS_LINK)
        self.click(self.SAVE_BUTTON)