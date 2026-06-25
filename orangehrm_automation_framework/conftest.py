import os
import pytest
import datetime
from utils.browser_factory import BrowserFactory
from utils.screenshot_util import ScreenshotUtil
from utils.video_recorder import VideoRecorder
from utils.logger_util import LoggerUtil
from utils.config_reader import ConfigReader

logger = LoggerUtil.get_logger()

@pytest.fixture(scope="class", autouse=True)
def setup_class(request):
    """Class-level fixture to load master config once."""
    config = ConfigReader.get_config()
    request.cls.config = config
    logger.info("Master configuration successfully loaded for class.")

@pytest.fixture(scope="function")
def driver(request):
    """Function-level fixture to initialize WebDriver and support tools."""
    config = ConfigReader.get_config()
    browser_name = config["framework"]["browser"]
    headless = config["framework"]["headless"]
    timeout = config["framework"]["timeout"]
    
    logger.info(f"Starting browser session: {browser_name} (Headless: {headless})")
    driver_instance = BrowserFactory.create_driver(browser_name, headless)
    driver_instance.implicitly_wait(timeout)
    driver_instance.maximize_window()
    
    # Initialize Video Recorder
    test_name = request.node.name
    recorder = None
    if config["framework"]["record_video"]:
        video_path = os.path.join("videos", f"{test_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
        recorder = VideoRecorder(video_path)
        recorder.start()
        logger.info(f"Started video recording for test: {test_name}")
        
    request.cls.driver = driver_instance
    
    yield driver_instance
    
    # Stop recording
    if recorder:
        recorder.stop()
        logger.info(f"Stopped video recording for test: {test_name}")
        
    # Capture Screenshot on Success (if configured)
    if config["framework"]["screenshot_on_success"]:
        ScreenshotUtil.capture_screenshot(driver_instance, f"{test_name}_success", passed=True)
        
    logger.info("Closing browser session")
    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.fixturenames:
                driver_instance = item.funcargs["driver"]
                test_name = item.name
                ScreenshotUtil.capture_screenshot(driver_instance, f"{test_name}_failed", passed=False)
                logger.error(f"Test {test_name} failed. Screenshot captured.")
        except Exception as e:
            logger.error(f"Failed to capture failure screenshot: {e}")