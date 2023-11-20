from christmas_history.histories_project.POM.tests.base_test import BaseTest


class TestHowDidChristmasStart(BaseTest):

    def test_how_did_christmas_start_navigation(self):
        self.navigate_to_how_did_christmas_start_tab()
        self.check_the_first_tab_paragraph_and_go_back()
