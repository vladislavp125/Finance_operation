from models.user import User
from models.account import Accaunt
import json


def add_js_file(user_id, data, name):
    with open(f"data/accounts/{user_id}.json", 'r') as file:
        data_op = json.load(file)
        for item in data_op:
            for key in item:
                if key == name:
                    print("Счет с таким именем уже существует!")
                    return None
        data_op.append(data[0])
    with open(f"data/accounts/{user_id}.json", 'w') as file:
        json.dump(data_op, file, indent=3)
    return data

def create_account(user_id, name, currency):
    data = [{name: [{"currency": currency, "balance": 0}]}]
    try:
        if add_js_file(user_id, data, name) is None:
            print("Счет с таким именем уже существует!")
            return data
        else:
            return data
    except FileNotFoundError:
        with open(f"data/accounts/{user_id}.json", 'w') as file:
            json.dump(data, file, indent=3)
            return data


def delete_account(account_id):
    pass


def update_account(account_id):
    operation = str(input("Ввыберите вид операции доход/расход (1/2): "))
    if operation == "1":
        amount = input("Введите сумму пополнения: ")
        name = input("Введите имя счета который нужно пополнить: ")
        with open(f"{account_id}.json", 'r') as file:
            data_op = json.load(file)
            for item in data_op:
                for key in item:
                    if key == name:
                        currency = item[key][0]['currency']
        account = Accaunt(account_id, name, currency)
        account.add_income(amount)
        new_balance = account.get_balance()
        account.balance = new_balance
        with open(f"{account_id}.json", 'r') as file:
            data_op = json.load(file)
            for item in data_op:
                for key in item:
                    if key == name:
                        print(item[key][0]['balance'])
                        item[key][0]['balance'] = new_balance
                        with open(f"{account_id}.json", 'w') as file:
                            json.dump(data_op, file, indent=3)
            return None

    else:
        amount = int(input("Введите сумму снятия: "))
        name = input("Введите имя счета c которого нужно снять деньги: ")
        with open(f"{account_id}.json", 'r') as file:
            data_op = json.load(file)
            for item in data_op:
                for key in item:
                    if key == name:
                        currency = item[key][0]['currency']

        account = Accaunt(account_id, name, currency)
        account.add_expense(amount)
        new_balance = account.get_balance()
        account.balance = new_balance
        with open(f"{account_id}.json", 'r') as file:
            data_op = json.load(file)
            for item in data_op:
                for key in item:
                    if key == name:
                        item[key][0]['balance'] = new_balance
                        with open(f"{account_id}.json", 'w') as file:
                            json.dump(data_op, file, indent=3)

            return None


def search_check(login, name):
    with open(f"data/accounts/{login}.json", 'r') as file:
        data_op = json.load(file)
        for item in data_op:
            for key in item:
                if key == name:
                    return item[key][0]['currency']
        return None


def get_balance_(user_id, name):
    with open(f"data/accounts/{user_id}.json", 'r') as file:
        data_op = json.load(file)
        for item in data_op:
            for key in item:
                if key == name:
                    return item[key][0]["balance"]


#while True:
#    user_id = input("Введите id счета")
#    #currency = input("выберите валюту счета(RUB/$): ")
#    #create_account(user_id, name, currency)
#    try:
#        update_account(user_id)
#    except FileNotFoundError:
#        print("файл не найден, попробуйте ещё раз")
#