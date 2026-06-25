from utils.common_actions import CommonActions
from utils.wait_util import WaitUtil

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=15):
        CommonActions.click_element(self.driver, locator, timeout)

    def write(self, locator, text, timeout=15):
        CommonActions.enter_text(self.driver, locator, text, timeout)

    def get_text(self, locator, timeout=15):
        return CommonActions.get_element_text(self.driver, locator, timeout)

    def is_visible(self, locator, timeout=5):
        return CommonActions.is_element_displayed(self.driver, locator, timeout)

    def select_dropdown(self, locator, text, timeout=15):
        CommonActions.select_dropdown_by_text(self.driver, locator, text, timeout)

    def select_custom_dropdown_option(self, dropdown_locator, option_text, timeout=15):
        CommonActions.select_custom_dropdown(self.driver, dropdown_locator, option_text, timeout)