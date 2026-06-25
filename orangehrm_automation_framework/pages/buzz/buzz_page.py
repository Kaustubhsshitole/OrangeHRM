from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuzzPage(BasePage):
    POST_TEXTAREA = (By.CSS_SELECTOR, "textarea.orangehrm-buzz-post-input")
    POST_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LIKE_ICON = (By.CSS_SELECTOR, "i.oxd-icon.bi-heart")

    def publish_post(self, text):
        self.write(self.POST_TEXTAREA, text)
        self.click(self.POST_BUTTON)

    def like_first_post(self):
        if self.is_visible(self.LIKE_ICON):
            self.click(self.LIKE_ICON)