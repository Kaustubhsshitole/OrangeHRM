from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil:
    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=15):
        """Blocks execution until locator element is visible on DOM."""
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=15):
        """Blocks execution until element is enabled and clickable."""
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_element_present(driver, locator, timeout=15):
        """Blocks execution until element exists in DOM schema, visible or not."""
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    @staticmethod
    def wait_for_text_to_be_present(driver, locator, text, timeout=15):
        """Blocks execution until specific content string exists in element."""
        return WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))