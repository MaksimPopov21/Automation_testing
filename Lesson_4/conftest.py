import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
s = Service('C:\\chromedriver\\chromedriver.exe')


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en', help="Specify the language for the tests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.mark.parametrize('language')
# def language_parametrize(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
#     browser.get(link)
