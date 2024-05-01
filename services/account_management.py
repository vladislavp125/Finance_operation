import asyncio
import random
import json
from utils.file_handler import *
import asyncio
from utils.currency_converter import get_currency
from utils.logger import *


@crate_account_log
def create_account(user_id, name, currency):
    try:
        data = get_data()
        for account in data:
            if account["user"] == user_id:
                if account["currency"] == currency:
                    print(f"Счет в такой валюте уже создан")
                    return None
                else:
                    continue
        id = random.randint(1, 99999)
        account = {"id": id, "name": name, "user": user_id, "currency": currency, "balance": 0}
        data.append(account)
        pull_data(data)
        print("Счет успешно создан")
        return id
    except FileNotFoundError:
        id = random.randint(1, 99999)
        account = [{"id": id, "name": name, "user": user_id, "currency": currency, "balance": 0}]
        pull_data(account)
        return id


@delete_account_log
def delete_account(account_id, login):
    data = get_data()
    for account in data:
        try:
            if account["id"] == int(account_id):
                data.remove(account)
                pull_data(data)
                print(f"Счет id: {account_id} name: {account["name"]}, валюта:{account["currency"]}, был успешно удален!")
                return True
            else:
                continue
        except ValueError:
            print("Некоректно введенный номер счета")
            return login
    print("Счет не найден!")
    return login


@transaction_income_log
def income_account(account_id, amount, login):
    data = get_data()
    for account in data:
        try:
            if account["id"] == int(account_id):
                account_balance = float(account["balance"])
                account_balance += float(amount)
                account["balance"] = account_balance
                pull_data(data)
                print(f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                      f"валюта:{account["currency"]}, баланс: {account["balance"]}")
                print()
                return True
        except ValueError:
            print("Некорректный ввод")
            return login
    print("Счет не найден!")
    return login


@transaction_expense_log
def expense_account(account_id, amount, login):
    data = get_data()
    for account in data:
        try:
            if account["id"] == int(account_id):
                account_balance = int(account["balance"])
                if int(amount) > account_balance:
                    print("Недостаточно средств на балансе")
                    return login
                account_balance -= int(amount)
                account["balance"] = account_balance
                pull_data(data)
                print(
                    f"Выполнен расход по балансу, Информация по счету: id: {account_id} name: {account["name"]}, "
                    f"валюта:{account["currency"]}, баланс: {account["balance"]}")
                return True
        except ValueError:
            print("Некорректный ввод")
            return login
    print("Счет не найден!")
    return login


@transaction_transfer_log
def transfer_account(account_id, to_account_id, amount, login):
    data = get_data()
    try:
        amount = float(amount)
        for account in data:
            if account["id"] == int(account_id):
                if account["user"] == login:
                    account_balance = float(account["balance"])
                    if amount > account_balance:
                        print("Недостаточно средств на балансе")
                        return login
                    account_balance -= float(amount)
                    account["balance"] = format(account_balance, '.2f')
                    pull_data(data)
                    currency_for_transfer = account["currency"]
                    print(
                        f"Выполнен расход по балансу, Информация по счету: id: {account_id} name: {account["name"]}, "
                        f"баланс: {account["balance"]} {account["currency"]}")
                    print()
                    if currency_for_transfer == "R":
                        data = get_data()
                        for account in data:
                            if account["id"] == int(to_account_id):
                                if account["currency"] == "R":
                                    account_balance = float(account["balance"])
                                    account_balance += float(amount)
                                    account["balance"] = format(account_balance, '.2f')
                                    pull_data(data)
                                    print(f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                                          f"баланс: {account["balance"]} {account["currency"]}")
                                    print()
                                    return True
                                elif account["currency"] == "$":
                                    currency_now = asyncio.run(get_currency())
                                    amount /= float(currency_now)
                                    account_balance = float(account["balance"])
                                    account_balance += float(amount)
                                    account["balance"] = format(account_balance, '.2f')
                                    pull_data(data)
                                    print(f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                                          f"баланс: {account["balance"]} {account["currency"]}")
                                    print()
                                    return True
                    elif currency_for_transfer == "$":
                        data = get_data()
                        for account in data:
                            if account["id"] == int(to_account_id):
                                if account["currency"] == "R":
                                    currency_now = float(asyncio.run(get_currency()))
                                    amount *= currency_now
                                    account_balance = float(account["balance"])
                                    account_balance += float(amount)
                                    account["balance"] = format(account_balance, '.2f')
                                    pull_data(data)
                                    print(
                                        f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                                        f"баланс: {account["balance"]} {account["currency"]}")
                                    return True
                                elif account["currency"] == "$":
                                    account_balance = float(account["balance"])
                                    account_balance += float(amount)
                                    account["balance"] = format(account_balance, '.2f')
                                    pull_data(data)
                                    print(
                                        f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                                        f"баланс: {account["balance"]} {account["currency"]}")
                                    return True
                else:
                    print("Нет доступа к этому счету!")
                    print()
        print("Счет не найден!")
        return login
    except ValueError:
        print("Некорректный ввод!")
        return login

