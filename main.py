from models.user import User
from models.account import Accaunt
from services.transaction_management import *



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
                print()
                print("Неверно указана валюта можно выбрать только 'R' или '$'")
                print()
                continue
        elif operation_auth == "2":
            account_id = input("Укажите ID вашего счета: ")
            transaction = input("Выберите формат операции income(1)/expense(2)/transfer(3): ")
            amount = input("Укажите сумму: ")
            add_transaction(account_id, amount, transaction, login)

        elif operation_auth == "3":
            account_id = input("Укажите ID счета по которому хотите узнать информацию: ")
            get_history_transactions(user.username, account_id)


        elif operation_auth == "4":
            account_id = input("Укажите id аккаунта по которому нужно предоставить отчет: ")
            print()
            start_date = input("Укажите дату в формате '2024-12-31 00:00:00' от которой будем считать: ")
            print()
            end_date = input("Укажите дату в формате '2024-12-31 00:00:00' до которой будем считать: ")
            get_transactions(user.username, account_id, start_date, end_date)


        elif operation_auth == "5":
            account_id = input("Укажите id аккаунта который нужно удалить: ")
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
        if user.auth == 1:
            print("Вход успешно выполнен!")
            print()
            print(f"Добро пожаловать user{user.username}")
            print()
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
            print()
            auth_user(user.username)