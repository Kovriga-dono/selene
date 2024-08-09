from selene.api import s, browser
import re
import models.lib
import allure


# заполняем контактные данные
def fill_contact_name():
    with allure.step('filling name'):
        s(models.lib.firstname_selector).set(models.lib.contact.first_name)


def fill_contact_lastname():
    with allure.step('filling lastname'):
        s(models.lib.lastname_selector).set(models.lib.contact.last_name)


def filling_category():
    with allure.step('filling category'):
        s(models.lib.category_selector).click()
        s(models.lib.category_selector_next).click()


def filling_birthday():
    with allure.step('filling birthday'):
        s(models.lib.birthday_selector).set(models.lib.contact.birthday)
        s(models.lib.firstname_selector).click()


def filling_addres():
    with allure.step('filling addres'):
        # берем оригинальное значение счетчика
        c = re.search(r'\d+$', s(models.lib.counter_selector).text).group()
        s(models.lib.addres_selector).set(models.lib.contact.address)
        s(models.lib.button_selector).click()
        # берём счетчик после создания контакта
        b = re.search(r'\d+$', s(models.lib.counter_selector).text).group()
    # сравниваем счетчик до и после создания контакта
    assert int(b) == int(c) + 1


def open_browser():
    with allure.step('open page'):
        browser.open_url('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')
