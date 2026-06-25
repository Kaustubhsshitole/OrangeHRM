from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CorporateBrandingPage(BasePage):
    BRAND_LINK = (By.XPATH, "//a[text()='Corporate Branding']")
    PRIMARY_COLOR_PICKER = (By.CSS_SELECTOR, "div.orangehrm-color-input")
    PUBLISH_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")

    def edit_branding(self):
        self.click(self.BRAND_LINK)
        # Select custom secondary branding components...
        self.click(self.PUBLISH_BUTTON)