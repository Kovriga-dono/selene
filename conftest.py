from selene.api import *
import pytest


def pytest_addoption(parser):
    parser.addoption("--remote", action="store_true", default=False, help="Запустить браузер удаленно")
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера для запуска тестов")


@pytest.fixture()
def browser_c():
    config.driver_name = 'chrome'
    config.window_width = 1024
    config.window_height = 768


@pytest.fixture()
def browser_f():
    config.driver_name = 'firefox'
    config.window_width = 1024
    config.window_height = 768
