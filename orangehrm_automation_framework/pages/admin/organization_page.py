from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrganizationPage(BasePage):
    ORG_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Organization ')]")
    LOCATIONS_LINK = (By.XPATH, "//a[text()='Locations']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    LOC_NAME_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "div.oxd-select-text")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def navigate_to_locations(self):
        self.click(self.ORG_DROPDOWN)
        self.click(self.LOCATIONS_LINK)

    def create_location(self, name, country):
        self.click(self.ADD_BUTTON)
        self.write(self.LOC_NAME_INPUT, name)
        self.select_custom_dropdown_option(self.COUNTRY_DROPDOWN, country)
        self.click(self.SAVE_BUTTON)