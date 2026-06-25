import pytest
from pages.login_page import LoginPage
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.employee_list_page import EmployeeListPage
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

@pytest.mark.usefixtures("driver")
class TestPIMEmployeeList:
    def test_create_and_verify_employee(self):
        """CRUD - Create & Read: Comprehensive employee onboarding and check."""
        logger.info("Executing test_create_and_verify_employee")
        driver = self.driver
        login_page = LoginPage(driver)
        add_emp = AddEmployeePage(driver)
        emp_list = EmployeeListPage(driver)

        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        # Onboard Employee
        add_emp.add_employee_with_credentials(
            self.config["test_data"]["employee"]["first_name"],
            self.config["test_data"]["employee"]["last_name"],
            self.config["test_data"]["employee"]["username"],
            self.config["test_data"]["employee"]["password"]
        )
        logger.info("Employee record successfully added to PIM.")

        # Search Employee
        emp_list.search_employee(self.config["test_data"]["employee"]["search_name"])
        logger.info("Search filter operation completed.")