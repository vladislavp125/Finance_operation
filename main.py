from models.user import User
from models.account import Accaunt
from services.transaction_management import *
import json


def auth_user(login):
    while True:
        print("МЕНЮ:")
        print("1. Открыть новый счет $ ")
        print("2. Добавление транзакций (Доходы, расходы)")
        print("3. История транзакций по счтеу")
        print("4. Генерация отчета по транзакциям")
        print("5. Удаление счета")
        print("6. Выйти")
        operation_auth = input()
        if operation_auth == "1":
            name = input("Введите название счета: ")
            currency = input("Выберите волюту 'R'/'$': ")
            if currency == "R" or "$":
                account = Accaunt(login, name, currency)
                account.create_account()
            else:
                print("Неверно указана валюта можно выбрать только 'R' или '$'")
                print()
                continue
        elif operation_auth == "2":
            account_id = int(input("Укажите ID вашего счета: "))
            transaction = input("Выберите формат операции income(1)/expense(2)/transfer(3): ")
            amount = float(input("Укажите сумму: "))
            add_transaction(account_id, amount, transaction, login)

        elif operation_auth == "3":
            pass
        elif operation_auth == "4":
            pass
        elif operation_auth == "5":
            account_id = int(input("Укажите id аккаунта который нужно удалить: "))
            account = Accaunt(login)
            account.delete_account(account_id)
        elif operation_auth == "6":
            user.auth = 0
            break


while True:
    operation = input('1(Войти)/2(Регистрация): ')

    if operation == '1':
        login = str(input("Введите логин: "))
        password = input("Введите пароль: ")
        user = User(login, password)
        user.login()
        print(user.auth)
        if user.auth == 1:
            print("Вход успешно выполнен!")
            print()
            print(f"Добро пожаловать user{user.username}")
            auth_user(user.username)

    elif operation == "2":
        login = input("Введите логин: ")
        password = input("Придумайте пароль: ")
        email = input("Укажите email: ")
        user = User(login, password, email)
        user.register()
        if user.auth == 1:
            print("Регистрация успешно завершена!")
            print()
            print(f"Добро пожаловать user-login: {user.username}")
            auth_user(user.username)