from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.oxd-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.oxd-alert-content p")
    
    def login(self, username, password):
        self.write(self.USERNAME_INPUT, username)
        self.write(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)