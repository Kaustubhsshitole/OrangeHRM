from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PerformanceConfigurePage(BasePage):
    CONFIG_DROPDOWN = (By.XPATH, "//span[contains(text(), 'Configure ')]")
    KPIS_LINK = (By.XPATH, "//a[text()='KPIs']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    KPI_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def create_kpi(self, title):
        self.click(self.CONFIG_DROPDOWN)
        self.click(self.KPIS_LINK)
        self.click(self.ADD_BUTTON)
        self.write(self.KPI_INPUT, title)
        self.click(self.SAVE_BUTTON)