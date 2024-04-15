from models import user
from services.account_management import *
from models.account import Accaunt
import json



while True:
    operation = input('1(Войти)/2(Регистрация): ')
    if operation == '1':
        login = str(input("Введите логин: "))
        password = input("Введите пароль: ")
        user_o = user.User(login, password)
        user_o.login()
        if user_o.auth == 1:
            print("Вход успешно выполнен!")
            print()
            print(f"Добро пожаловать user{user_o.username}")
            while True:
                print("МЕНЮ:")
                print("1. Открыть новый счет $ ")
                print("2. Баланс по вашему счету")
                print("3. Добавление транзакций (Доходы, расходы, переводы между своими счетами)")
                print("4. История транзакций по счтеу")
                print("5. Генерация отчета по транзакциям")
                operation_auth = input()
                if operation_auth == "1":
                    user_id = input("Введите id счета")
                    currency = input("Введите валюту RUB/$: ")
                    chek = create_account(login, user_id, currency)
                    print(f"Открыт счет: name:{list(chek[0])[0]}, Баланс: {chek[0][user_id][0]['balance']} {chek[0][user_id][0]['currency']}")
                elif operation_auth == "2":
                    user_id = input("Введите id счета")
                    currency = search_check(login, user_id)
                    if currency is not None:
                        account = Accaunt(login, user_id, currency)
                        account.get_balance()


    elif operation == "2":
        login = input("Введите логин: ")
        password = input("Придумайте пароль: ")
        email = input("Укажите email: ")
        user_o = user.User(login, password, email)
        user_o.register()
        if user_o.auth == 1:
            print("Регистрация успешно завершена!")
            print()
            print(f"Добро пожаловать user{user_o.username}")
            while True:
                print("Авторизован")
                break