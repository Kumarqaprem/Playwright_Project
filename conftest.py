import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    yield page
    context.close()
