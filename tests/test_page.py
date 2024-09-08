import pages.main_page
from conftest import browser_c, browser_f
import allure


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
    pages.main_page.end_test()


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
    pages.main_page.end_test()
