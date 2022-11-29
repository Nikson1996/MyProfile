# MyProfile app

SEPARATOR = "-" * 40

# personal information
name = ""
age = 0
phone_number = ""
email = ""
postal_code = ""
adress = ""
additional_information = ""

# bank requisites
requisite = 0
taxpayer_identification_number = 0
payment_account = 0
bank_name = ""
bank_identification_code = 0
correspondent_account = 0

print("Приложение MyProfile\nСохраняй информацию о себе и выводи ее в разных форматах")
while True:
    # main menu
    print(SEPARATOR)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию")
    print("2 - Вывести информацию")
    print("0 - Завершить работу")

    action_main_menu = input("Введите номер пункта меню: ")
    if action_main_menu == "0":
        break
    elif action_main_menu == "1":
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Информация о предпринимателе")
            print("0 - Назад")
            action_add_menu = input("Введите номер пункта меню: ")
            if action_add_menu == "1":
                # input general info
                name = input("Введите имя: ")
                while True:
                    age = int(input("Введите возраст: "))
                    if age > 0:
                        break
                    print("Некорректные данные, введите положительное число")
                phone_number = input("Введите номер телефона (+7ХХХХХХХХХХ): ")
                email = input("Введите адрес электронной почты: ")
                post_code = input("Введите почтовый индекс: ")
                for sym in post_code:
                    if sym.isdigit():
                        postal_code += sym
                adress = input("Введите почтовый адрес без(индекса): ")
                additional_information = input("Введите дополнительную информацию: ")
            if action_add_menu == "2":
                # input bank requisites
                while True:
                    requisite = int(input("Введите ОГРНИП: "))
                    if len(str(requisite)) == 15:
                        break
                    print("ОГРНИП должен содержать 15 цифр")
                taxpayer_identification_number = int(input("Введите ИНН: "))
                while True:
                    payment_account = int(input("Введите расчетный счет: "))
                    if len(str(payment_account)) == 20:
                        break
                    print("Расчетный счет должен содержать 20 цифр")
                bank_name = input("Название банка: ")
                bank_identification_code = int(input("Введите БИК: "))
                correspondent_account = int(input("Введите корреспондентский счет: "))
            if action_add_menu == "0":
                break
    elif action_main_menu == "2":
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print("ВЫВЕСТИ ИНФОРМАЦИЮ")
            print("1 - Общая информация")
            print("2 - Вся информация")
            print("0 - Назад")
            action_information_menu = input("Введите номер пункта меню: ")
            if action_information_menu == "0":
                break
            elif action_information_menu == "1":
                # print general information
                print(SEPARATOR)
                print(
                    f"Имя: {name}\nВозраст: {age}\nТелефон: {phone_number}\nE-mail: {email}\nИндекс: {postal_code}\nАдрес: {adress}")
            elif action_information_menu == "2":
                # print full information
                print(SEPARATOR)
                print(
                    f"Имя: {name}\nВозраст: {age}\nТелефон: {phone_number}\nE-mail: {email}\nИндекс: {postal_code}\nАдрес: {adress}")
                print()
                print(f"Информация о предпринимателе\nОГРНИП: {requisite}\nИНН: {taxpayer_identification_number}")
                print(
                    f"Банковские реквизиты\nР/с: {payment_account}\nБанк: {bank_name}\nБИК: {bank_identification_code}\nК/с: {correspondent_account}")
            else:
                print("Введите корректный пункт меню")
    else:
        print("Введите корректный пункт меню")
