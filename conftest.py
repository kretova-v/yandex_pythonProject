import pytest
from playwright.sync_api import Playwright

from page_objects.main_page import MainPage


@pytest.fixture(scope="function")
def browser(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('ng-repeat')
    browser = playwright.chromium.launch(headless=False)
    return browser

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    return page

@pytest.fixture(scope="function")
def main_page(page):
    return MainPage(page)
