import pytest
from pages.login_page import LoginPage
from pages.time.attendance_page import AttendancePage
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

@pytest.mark.usefixtures("driver")
class TestTimeTimesheets:
    def test_attendance_punch_in_out(self):
        """Positive - Verifies a check-in sequence with comments in attendance module."""
        logger.info("Executing test_attendance_punch_in_out")
        driver = self.driver
        login_page = LoginPage(driver)
        att_page = AttendancePage(driver)

        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        att_page.punch_in_out("Automated Test Attendance Entry.")
        logger.info("Punch In sequence completed.")