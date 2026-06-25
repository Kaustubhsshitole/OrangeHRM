from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class VacanciesPage(BasePage):
    VACANCIES_LINK = (By.XPATH, "//a[text()='Vacancies']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    NAME_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def create_vacancy(self, name):
        self.click(self.VACANCIES_LINK)
        self.click(self.ADD_BUTTON)
        self.write(self.NAME_INPUT, name)
        self.click(self.SAVE_BUTTON)