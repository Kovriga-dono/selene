from selene.support.shared import browser
import pytest


def pytest_addoption(parser):
    parser.addoption("--remote", action="store_true", default=False, help="Запустить браузер удаленно")
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера для запуска тестов")


# def pytest_addoption(parser):
#     parser.addoption("--remote", default=False, action='store_true',
#                      help="Передаем - если надо запустить браузер удаленно")


@pytest.fixture()
def browser_c():
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture()
def browser_f():
    browser.config.driver_name = 'firefox'
    browser.config.window_width = 1024
    browser.config.window_height = 768
