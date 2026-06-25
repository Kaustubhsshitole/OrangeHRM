from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SubmitClaimPage(BasePage):
    SUBMIT_CLAIM_LINK = (By.XPATH, "//a[text()='Submit Claim']")
    EVENT_DROPDOWN = (By.XPATH, "//label[text()='Event']/ancestor::div[1]//div[@class='oxd-select-text']")
    CURRENCY_DROPDOWN = (By.XPATH, "//label[text()='Currency']/ancestor::div[1]//div[@class='oxd-select-text']")
    REMARKS_TEXT = (By.CSS_SELECTOR, "textarea.oxd-textarea")
    CREATE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def create_claim(self, event, currency, remarks):
        self.click(self.SUBMIT_CLAIM_LINK)
        self.select_custom_dropdown_option(self.EVENT_DROPDOWN, event)
        self.select_custom_dropdown_option(self.CURRENCY_DROPDOWN, currency)
        self.write(self.REMARKS_TEXT, remarks)
        self.click(self.CREATE_BUTTON)