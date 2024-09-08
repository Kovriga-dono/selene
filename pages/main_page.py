from selene.support.shared.jquery_style import s
from selene.support.shared import browser
from selene import query
import re
from models import locators, data
import allure


# заполняем контактные данные
def fill_contact_name():
    with allure.step('filling name'):
        s(locators.firstname_selector).set(data.contact.first_name)


def fill_contact_lastname():
    with allure.step('filling lastname'):
        s(locators.lastname_selector).set(data.contact.last_name)


def filling_category():
    with allure.step('filling category'):
        s(locators.category_selector).click()
        s(locators.category_selector_next).click()


def filling_birthday():
    with allure.step('filling birthday'):
        s(locators.birthday_selector).set(data.contact.birthday)
        s(locators.firstname_selector).click()


def filling_addres():
    with allure.step('filling addres'):
        # берем оригинальное значение счетчика
        c = re.search(r'\d+$', s(locators.counter_selector).get(query.text)).group()
        s(locators.addres_selector).set(data.contact.address)
        s(locators.button_selector).click()
        # берём счетчик после создания контакта
        b = re.search(r'\d+$', s(locators.counter_selector).get(query.text)).group()
    # сравниваем счетчик до и после создания контакта
    assert int(b) == int(c) + 1


def open_browser():
    with allure.step('open page'):
        browser.open('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')
