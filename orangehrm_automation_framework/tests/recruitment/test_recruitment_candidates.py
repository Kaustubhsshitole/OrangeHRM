import pytest
from pages.login_page import LoginPage
from pages.recruitment.candidates_page import CandidatesPage
from utils.logger_util import LoggerUtil

logger = LoggerUtil.get_logger()

@pytest.mark.usefixtures("driver")
class TestRecruitmentCandidates:
    def test_candidate_registration(self):
        """Positive - Adds a candidate profile into recruitment module."""
        logger.info("Executing test_candidate_registration")
        driver = self.driver
        login_page = LoginPage(driver)
        cand_page = CandidatesPage(driver)

        driver.get(self.config["framework"]["base_url"])
        login_page.login(
            self.config["test_data"]["login"]["valid_username"],
            self.config["test_data"]["login"]["valid_password"]
        )

        cand_page.create_candidate(
            self.config["test_data"]["recruitment"]["candidate_first_name"],
            self.config["test_data"]["recruitment"]["candidate_last_name"],
            self.config["test_data"]["recruitment"]["candidate_email"],
            self.config["test_data"]["recruitment"]["keywords"]
        )
        logger.info("Candidate onboarding transaction complete.")