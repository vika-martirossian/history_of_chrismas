from selenium.webdriver.common.by import By

from christmas_history.histories_project.POM.lib.helpers import Helpers
from christmas_history.histories_project.POM.lib.assertions import assert_that
from christmas_history.histories_project.testing_data.test_data import base_url


class SaturnaliaAndChristmas(Helpers):
    saturnalia_and_christmas_link = (By.ID, "saturnalia-and-christmas")

    def assert_paragraph_heading(self, expected_paragraph_heading="Saturnalia and Christmas "):
        actual_heading = self.find(self.saturnalia_and_christmas_link, get_text=True)
        assert_that(actual_heading == expected_paragraph_heading)

    def go_back_to_history_of_christmas(self):
        self.driver_back()
        actual_url = self.get_page_url()
        assert_that(actual_url == base_url)
