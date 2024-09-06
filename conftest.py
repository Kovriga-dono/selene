from selene.support.shared import browser
import pytest


@pytest.fixture()
def browser_c():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture()
def browser_f():
    browser.browser_name = 'firefox'
    browser.config.window_width = 1024
    browser.config.window_height = 768
