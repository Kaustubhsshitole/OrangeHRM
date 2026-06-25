from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QualificationsPage(BasePage):
    QUAL_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Qualifications ')]")
    SKILLS_LINK = (By.XPATH, "//a[text()='Skills']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    SKILL_NAME_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SKILL_DESC_INPUT = (By.XPATH, "//textarea[@placeholder='Type description here']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def navigate_to_skills(self):
        self.click(self.QUAL_DROPDOWN)
        self.click(self.SKILLS_LINK)

    def create_skill(self, name, description):
        self.click(self.ADD_BUTTON)
        self.write(self.SKILL_NAME_INPUT, name)
        self.write(self.SKILL_DESC_INPUT, description)
        self.click(self.SAVE_BUTTON)