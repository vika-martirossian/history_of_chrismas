from christmas_history.histories_project.POM.tests.base_test import BaseTest


class TestSaturnaliaAndChristmas(BaseTest):

    def test_saturnalia_and_christmas_navigation(self):
        self.navigate_to_saturnalia_and_christmas_tab()
        self.check_the_second_tab_paragraph_and_go_back()
