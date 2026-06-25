import pytest
from pages.login_page import LoginPage
from pages.leave.apply_leave_page import ApplyLeavePage
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

@pytest.mark.usefixtures("driver")
class TestLeaveApply:
    def test_apply_leave_form(self):
        """Positive - Submits a valid leave request within configured parameters."""
        logger.info("Executing test_apply_leave_form")
        driver = self.driver
        login_page = LoginPage(driver)
        apply_page = ApplyLeavePage(driver)

        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        apply_page.apply_leave(
            self.config["test_data"]["leave"]["leave_type"],
            self.config["test_data"]["leave"]["start_date"],
            self.config["test_data"]["leave"]["end_date"],
            self.config["test_data"]["leave"]["comment"]
        )
        logger.info("Leave submission sequence executed successfully.")