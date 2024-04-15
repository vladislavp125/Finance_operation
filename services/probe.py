import csv
import json


class User:
    def __init__(self, login, password):
        self.currency = None
        self.balance = None
        self.login = login
        self.password = password
        self.auth = 0
        self.name = None

    def user_auth(self):
        with open("data/users_data.csv", "r") as file:
            for line in file:
                if check_password(self.login, self.password):
                    temp = line.split("," or '\n')
                    self.balance = int(temp[2])
                    self.currency = temp[3]
                    self.auth = 1


    def user_sign(self):
        with open("data/users_data.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(
                [self.login, self.password, 0, "RUB"]
            )
            self.balance = 0
            self.currency = "RUB"
        with open("data/users_data.csv", 'r') as file:
            if self.login in file:
                print("Аккаунт с таким логином уже зарегистрирован.")

class Check:
    def __init__(self):
        self.name_check = None
        self.currency = None
        self.balance = 0

    def check_up(self):
        pass

    def check_down(self):
        pass

    def new_check(self):
        name_check = input("Введите назщвание счета: ")
        currency = input("Выберите валюту:")
        with open(f"check_data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(
                [user.login, name_check, currency, self.balance]
            )

    def info_check(self, login):
        with open(f"check_data.csv", "r") as file:
            for line in file:
                if login in line:
                    temp = line.split(",")
                    name_check, currency, self.balance = temp[0:]


user = User
check = Check


def file_check(login):
    with open("data/users_data.csv", "r") as file:
        for line in file:
            if login in line:
                return True


def check_password(login, password):
    if file_check(login):
        with open("data/users_data.csv", "r") as file:
            user_d = []
            for line in file:
                user_d.append(line.split(','))
                for user in user_d:
                    if login in user:
                        if password == user[1]:
                            return True


while True:
    print("Добро пожаловать!")
    o = str(input("Введи номер операции: "))
    if o == '1':
        login = str(input("Придумайте логин: "))
        password = str(input("Придумайте пароль: "))
        try:
            a = file_check(login)
            if a:
                print("Аккаунт с таким Логином уже существует!")
            else:
                user = User(login, password)
                user.user_sign()
                print(f"Вы успешно зарегистрировались Ваш логин:{login} Ваш баланс: {user.balance} Валюта: {user.currency}")
        except FileNotFoundError:
            user = User(login, password)
            user.user_sign()
            print(f"Вы успешно зарегистрировались Ваш логин:{login} Ваш баланс: {user.balance} Валюта: {user.currency}")

    elif o == '2':
        login = str(input("Придумайте логин: "))
        password = str(input("Придумайте пароль: "))
        user = User(login, password)
        user.user_auth()
        if user.auth == 1:
            while True:
                print(f'С возвращением, на вышем балансе: {user.balance} {user.currency}')
        else:
            print("Неверный пароль")

















