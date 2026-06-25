from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyClaimsPage(BasePage):
    MY_CLAIMS_LINK = (By.XPATH, "//a[text()='My Claims']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def view_my_claims(self):
        self.click(self.MY_CLAIMS_LINK)
        self.click(self.SEARCH_BUTTON)