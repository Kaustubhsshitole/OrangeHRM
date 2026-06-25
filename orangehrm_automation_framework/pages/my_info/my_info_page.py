from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyInfoPage(BasePage):
    PERSONAL_DETAILS_LINK = (By.XPATH, "//a[text()='Personal Details']")
    LICENSE_EXP_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")

    def edit_personal_details(self, date):
        self.click(self.PERSONAL_DETAILS_LINK)
        self.write(self.LICENSE_EXP_DATE, date)
        self.click(self.SAVE_BUTTON)