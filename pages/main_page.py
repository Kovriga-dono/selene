from selene.api import s, browser
import re
import models.locators
import models.data
import allure


# заполняем контактные данные
def fill_contact_name():
    with allure.step('filling name'):
        s(models.locators.firstname_selector).set(models.data.contact.first_name)


def fill_contact_lastname():
    with allure.step('filling lastname'):
        s(models.locators.lastname_selector).set(models.data.contact.last_name)


def filling_category():
    with allure.step('filling category'):
        s(models.locators.category_selector).click()
        s(models.locators.category_selector_next).click()


def filling_birthday():
    with allure.step('filling birthday'):
        s(models.locators.birthday_selector).set(models.data.contact.birthday)
        s(models.locators.firstname_selector).click()


def filling_addres():
    with allure.step('filling addres'):
        # берем оригинальное значение счетчика
        c = re.search(r'\d+$', s(models.locators.counter_selector).text).group()
        s(models.locators.addres_selector).set(models.data.contact.address)
        s(models.locators.button_selector).click()
        # берём счетчик после создания контакта
        b = re.search(r'\d+$', s(models.locators.counter_selector).text).group()
    # сравниваем счетчик до и после создания контакта
    assert int(b) == int(c) + 1


def open_browser():
    with allure.step('open page'):
        browser.open_url('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')
