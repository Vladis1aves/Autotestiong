import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

#
# @pytest.fixture(scope="function")
# def browser_chrome():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(15)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# @pytest.fixture(scope="function")
# def browser_firefox():
#     print("\nstart browser for test..")
#     browser = webdriver.Firefox()
#     browser.implicitly_wait(15)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
