from selenium.webdriver.common.by import By

from christmas_history.histories_project.POM.lib.helpers import Helpers
from christmas_history.histories_project.POM.lib.assertions import assert_that
from christmas_history.histories_project.testing_data.test_data import base_url


class HowDidChristmasStart(Helpers):
    how_did_christmas_start_text = (By.ID, "how-did-christmas-start")

    def assert_paragraph_heading(self, expected_paragraph_heading="How Did Christmas Start?"):
        actual_heading = self.find(self.how_did_christmas_start_text, get_text=True)
        assert_that(actual_heading == expected_paragraph_heading)

    def go_back_to_history_of_christmas(self):
        self.driver_back()
        actual_url = self.get_page_url()
        assert_that(actual_url == base_url)

