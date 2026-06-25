import pytest
from pages.login_page import LoginPage
from pages.admin.organization_page import OrganizationPage
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

@pytest.mark.usefixtures("driver")
class TestAdminOrganization:
    def test_add_location_success(self):
        """CRUD - Create: Validates creation of a physical office location."""
        logger.info("Executing test_add_location_success")
        driver = self.driver
        login_page = LoginPage(driver)
        org_page = OrganizationPage(driver)

        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        org_page.navigate_to_locations()
        org_page.create_location("Silicon Valley HQ", "United States")
        logger.info("Office location create transaction submitted successfully.")