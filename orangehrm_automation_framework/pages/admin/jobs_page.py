from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class JobsPage(BasePage):
    JOB_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Job ')]")
    JOB_TITLES_LINK = (By.XPATH, "//a[text()='Job Titles']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    JOB_TITLE_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    JOB_DESC_INPUT = (By.XPATH, "//textarea[@placeholder='Type description here']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    def navigate_to_job_titles(self):
        self.click(self.JOB_DROPDOWN)
        self.click(self.JOB_TITLES_LINK)

    def add_job_title(self, title, description):
        self.click(self.ADD_BUTTON)
        self.write(self.JOB_TITLE_INPUT, title)
        self.write(self.JOB_DESC_INPUT, description)
        self.click(self.SAVE_BUTTON)