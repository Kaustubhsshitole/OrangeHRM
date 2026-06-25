import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from utils.wait_util import WaitUtil
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

class CommonActions:
    @staticmethod
    def click_element(driver, locator, timeout=15):
        """Safely clicks on an element after confirming interactive state."""
        element = WaitUtil.wait_for_element_clickable(driver, locator, timeout)
        element.click()
        logger.debug(f"Clicked element with locator: {locator}")

    @staticmethod
    def enter_text(driver, locator, text, timeout=15):
        """Clears field and sends key codes with robust logs."""
        element = WaitUtil.wait_for_element_visible(driver, locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.debug(f"Entered text '{text}' into element: {locator}")

    @staticmethod
    def get_element_text(driver, locator, timeout=15):
        element = WaitUtil.wait_for_element_visible(driver, locator, timeout)
        text = element.text
        logger.debug(f"Retrieved text '{text}' from locator: {locator}")
        return text

    @staticmethod
    def is_element_displayed(driver, locator, timeout=5):
        try:
            element = WaitUtil.wait_for_element_visible(driver, locator, timeout)
            return element.is_displayed()
        except:
            return False

    @staticmethod
    def select_dropdown_by_text(driver, locator, text, timeout=15):
        element = WaitUtil.wait_for_element_visible(driver, locator, timeout)
        select = Select(element)
        select.select_by_visible_text(text)
        logger.debug(f"Selected text '{text}' from native select: {locator}")

    @staticmethod
    def select_custom_dropdown(driver, dropdown_locator, option_text, timeout=15):
        """Helper for custom listboxes styled in OrangeHRM .oxd-select-wrapper."""
        CommonActions.click_element(driver, dropdown_locator, timeout)
        time.sleep(0.5)
        from selenium.webdriver.common.by import By
        option_locator = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{option_text}')]")
        CommonActions.click_element(driver, option_locator, timeout)
        logger.debug(f"Selected custom dropdown option: '{option_text}'")