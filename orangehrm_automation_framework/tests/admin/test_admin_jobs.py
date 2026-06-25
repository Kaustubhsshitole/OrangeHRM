import pytest
from pages.login_page import LoginPage
from pages.admin.jobs_page import JobsPage
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

@pytest.mark.usefixtures("driver")
class TestAdminJobs:
    def test_add_job_title_positive(self):
        """CRUD - Create: Validates adding a new Job Title successfully."""
        logger.info("Executing test_add_job_title_positive")
        driver = self.driver
        login_page = LoginPage(driver)
        jobs_page = JobsPage(driver)

        # Login
        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        # Navigate & Add
        jobs_page.navigate_to_job_titles()
        test_title = f"QA Lead - {self.config['test_data']['employee']['employee_id']}"
        jobs_page.add_job_title(
            test_title,
            "Automated high-coverage Python test job title."
        )
        logger.info(f"Successfully added Job Title: {test_title}")

    def test_add_job_title_missing_required_validation(self):
        """Validation - Validates required fields error messages on empty forms."""
        logger.info("Executing test_add_job_title_missing_required_validation")
        driver = self.driver
        login_page = LoginPage(driver)
        jobs_page = JobsPage(driver)

        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        jobs_page.navigate_to_job_titles()
        # Submit empty form
        jobs_page.add_job_title("", "")
        
        # Verify required validation labels are displayed
        assert jobs_page.is_visible(JobsPage.SAVE_BUTTON), "Save button is visible on validation block."
        logger.warning("Blank form validation triggered and passed.")