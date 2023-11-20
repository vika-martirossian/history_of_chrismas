from selenium.webdriver.common.by import By

from christmas_history.histories_project.POM.lib.helpers import Helpers


class HistoryOfChristmas(Helpers):
    how_did_christmas_start_link = (By.LINK_TEXT, "How Did Christmas Start?")
    saturnalia_and_christmas_link = (By.XPATH, '//*[@href="#saturnalia-and-christmas"]')

    def click_on_christmas_start_link(self):
        self.find_and_click(self.how_did_christmas_start_link)

    def click_on_saturnalia_and_christmas_link(self):
        self.find_and_click(self.saturnalia_and_christmas_link)

