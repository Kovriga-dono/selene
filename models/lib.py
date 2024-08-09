from models.contact import Fields

# счетчик контактов
counter_selector = '//div[@dir="ltr"]'

# кнопка создания контакта
button_selector = '//div[@class="middleCenterInner"]/div/table/tbody/tr[7]/td/button[2]'

firstname_selector = '//div[@class="middleCenterInner"]/div/table/tbody/tr[2]/td[2]/input'
lastname_selector = '//div[@class="middleCenterInner"]/div/table/tbody/tr[3]/td[2]/input'
category_selector = '//div[@class="middleCenterInner"]/div/table/tbody/tr[4]/td[2]/select'
category_selector_next = '//div[@class="middleCenterInner"]/div/table/tbody/tr[4]/td[2]/select/option[2]'
birthday_selector = '//div[@class="middleCenterInner"]/div/table/tbody/tr[5]/td[2]/input'
addres_selector = '//div[@class="middleCenterInner"]/div/table/tbody/tr[6]/td[2]/textarea'


contact = Fields("John",
                 "Doe",
                 "Family",
                 "Baker street 1337",
                 "June 11, 2001")

