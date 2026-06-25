from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h6.oxd-topbar-header-breadcrumb-module")
    WIDGETS = (By.CSS_SELECTOR, ".orangehrm-dashboard-widget")
    
    def get_header_text(self):
        return self.get_text(self.HEADER)

    def get_widget_count(self):
        elements = self.driver.find_elements(*self.WIDGETS)
        return len(elements)

    def navigate_to_module(self, module_name):
        locator = (By.XPATH, f"//span[text()='{module_name}']")
        self.click(locator)