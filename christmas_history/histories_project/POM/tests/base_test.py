import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_how_did_christmas_start_tab(self):
        self.historyofchristmas.click_on_christmas_start_link()

    def check_the_first_tab_paragraph_and_go_back(self):
        self.howdidchristmasstart.assert_paragraph_heading()
        self.howdidchristmasstart.go_back_to_history_of_christmas()

    def navigate_to_saturnalia_and_christmas_tab(self):
        self.historyofchristmas.click_on_saturnalia_and_christmas_link()

    def check_the_second_tab_paragraph_and_go_back(self):
        self.saturnaliaandchristmas.assert_paragraph_heading()
        self.saturnaliaandchristmas.go_back_to_history_of_christmas()


