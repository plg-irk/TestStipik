import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # Объявляем параметр для запуска
    parser.addoption('--user_language', action='store', default="en",
                     help="en or ru")


@pytest.fixture(scope="function")
def browser(request):
    print("\nStart test..")
    user_language = request.config.getoption("user_language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
