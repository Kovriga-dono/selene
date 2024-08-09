import pages.main_page
from conftest import browser_c, browser_e, browser_s, browser_f
import allure
import os


# тесты для Chrome и FireFox будут запускаться для Winows, MacOS и Linux
# запускает тест для браузера Chome
@allure.feature('autotest example')
@allure.story('filling Chrome')
def test_fill_contact(browser_c):
    with allure.step('open Chrome'):
        pages.main_page.open_browser()
    pages.main_page.fill_contact_name()
    pages.main_page.fill_contact_lastname()
    pages.main_page.filling_category()
    pages.main_page.filling_birthday()
    pages.main_page.filling_addres()


# запускает тест для браузера FireFox
@allure.feature('autotest example')
@allure.story('filling FireFox')
def test_fill_contact_f(browser_f):
    with allure.step('open browser FireFox'):
        pages.main_page.open_browser()
    pages.main_page.fill_contact_name()
    pages.main_page.fill_contact_lastname()
    pages.main_page.filling_category()
    pages.main_page.filling_birthday()
    pages.main_page.filling_addres()


# EDGE тестируем только для Windows
if os.name == 'nt':
    # запускает тест для браузера EDGE
    @allure.feature('autotest example')
    @allure.story('filling Edge')
    def test_fill_contact_e(browser_e):
        with allure.step('open browser Edge'):
            pages.main_page.open_browser()
        pages.main_page.fill_contact_name()
        pages.main_page.fill_contact_lastname()
        pages.main_page.filling_category()
        pages.main_page.filling_birthday()
        pages.main_page.filling_addres()


# Safari тестируем только в MacOS
elif os.name == 'mac':
    # запускает тест для браузера EDGE
    @allure.feature('autotest example')
    @allure.story('filling Safari')
    def test_fill_contact_m(browser_s):
        with allure.step('open Safari'):
            pages.main_page.open_browser()
        pages.main_page.fill_contact_name()
        pages.main_page.fill_contact_lastname()
        pages.main_page.filling_category()
        pages.main_page.filling_birthday()
        pages.main_page.filling_addres()
