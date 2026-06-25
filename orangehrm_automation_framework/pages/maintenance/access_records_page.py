from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccessRecordsPage(BasePage):
    ACCESS_LINK = (By.XPATH, "//a[text()='Access Records']")
    EMP_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")

    def download_access_record(self, name):
        self.click(self.ACCESS_LINK)
        self.write(self.EMP_NAME, name)
        self.click(self.DOWNLOAD_BUTTON)