from selene import config
from selene.browser import driver
import pytest


@pytest.fixture()
def browser_c():
    config.browser_name = 'chrome'
    driver().set_window_size(1024, 768)


@pytest.fixture()
def browser_f():
    config.browser_name = 'firefox'
    driver().set_window_size(1024, 768)
