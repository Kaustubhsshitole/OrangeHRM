from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CandidatesPage(BasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.XPATH, "//label[text()='Email']/ancestor::div[1]//input")
    KEYWORDS = (By.XPATH, "//label[text()='Keywords']/ancestor::div[1]//input")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def create_candidate(self, fname, lname, email, keywords):
        self.click(self.ADD_BUTTON)
        self.write(self.FIRST_NAME, fname)
        self.write(self.LAST_NAME, lname)
        self.write(self.EMAIL, email)
        self.write(self.KEYWORDS, keywords)
        self.click(self.SAVE_BUTTON)