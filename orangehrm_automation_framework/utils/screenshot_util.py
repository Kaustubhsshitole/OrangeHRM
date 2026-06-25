import os
import datetime
from utils.config_reader import ConfigReader

class ScreenshotUtil:
    @staticmethod
    def capture_screenshot(driver, screenshot_name, passed=True):
        """Saves current driver view to screenshot directory structure."""
        config = ConfigReader.get_config()
        path_key = "passed_screenshots" if passed else "failed_screenshots"
        screenshot_dir = config["framework"]["paths"][path_key]
        
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
            
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshot_name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)
        
        driver.save_screenshot(filepath)
        return filepath