from selene import config
import pytest


@pytest.fixture()
def browser_c():
    config.browser_name = 'chrome'


@pytest.fixture()
def browser_e():
    config.browser_name = 'edge'


@pytest.fixture()
def browser_f():
    config.browser_name = 'firefox'


@pytest.fixture()
def browser_s():
    config.browser_name = 'safari'
