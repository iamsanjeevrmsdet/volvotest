import pytest
import json
from selenium import webdriver
from screenshot_utils import take_screenshot
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    
    request.cls.driver = driver
    yield
    driver.quit()

# Hook to capture screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        # Get the driver from the test class
        driver = item.instance.driver
        # Take a screenshot if the test failed
        take_screenshot(driver, name=item.name)


def load_json_data(file_path):
    with open(file_path) as f:
        return json.load(f)

@pytest.fixture(scope="module")
def get_test_data():
    data = load_json_data("test_data.json")
    return data

