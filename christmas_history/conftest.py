
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from christmas_history.histories_project.POM.pages.history_of_christmas_page import HistoryOfChristmas
from christmas_history.histories_project.POM.pages.how_did_christmas_start_tab import HowDidChristmasStart
from christmas_history.histories_project.POM.pages.saturnalia_and_christmas_tab import SaturnaliaAndChristmas
from histories_project.testing_data import test_data

driver = None

"""def pytest_addoption(parser):: 
This function defines a custom hook provided by 
Pytest for adding command-line options. 
It takes one argument, parser, 
which is used to add the custom option.

parser.addoption("--browser", action="store", default=test_data.browser): Within the pytest_addoption function, you are using the parser object to define the --browser command-line option.

--browser: This is the name of the command-line option you are defining. Users can specify the browser they want to use by providing this option, followed by the browser name (e.g., --browser chrome).

action="store": This parameter specifies the action to take when the --browser option is used. In this case, it stores the value provided for --browser as a string."""

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=test_data.browser)

"""request is an object provided by pytest that contains information about the test being run, including access to the pytest configuration.
   
   request.config gives you access to the pytest configuration, including any command-line options that were passed when running the test.
   
   .getoption("--browser") is used to retrieve the value associated with the --browser command-line option. This command-line option might be used to 
   
   specify which web browser to use for your test."""

@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    elif get_browser == "headless":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Driver not supported")
    driver.implicitly_wait(10)
    # Add in here each page from the POM in order to initialize the driver for each one.
    request.cls.historyofchristmas = HistoryOfChristmas(driver)
    request.cls.howdidchristmasstart = HowDidChristmasStart(driver)
    request.cls.saturnaliaandchristmas = SaturnaliaAndChristmas(driver)
    driver.get(test_data.base_url)
    yield driver
    driver.quit()




