import asyncio
import random
import json
from utils.file_hendler import *
import asyncio
from utils.currency_converter import get_currency


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
        return None
    except FileNotFoundError:
        id = random.randint(1, 99999)
        account = [{"id": id, "name": name, "user": user_id, "currency": currency, "balance": 0}]
        pull_data(account)


def delete_account(account_id):
    data = get_data()
    for account in data:
        if account["id"] == account_id:
            data.remove(account)
            pull_data(data)
            print(f"Счет id: {account_id} name: {account["name"]}, валюта:{account["currency"]}, был успешно удален!")
            return None
        else:
            continue
    print("Счет не найден!")
    return None


def income_account(account_id, amount):
    data = get_data()
    for account in data:
        if account["id"] == account_id:
            account_balance = int(account["balance"])
            account_balance += int(amount)
            account["balance"] = account_balance
            pull_data(data)
            print(f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                  f"валюта:{account["currency"]}, баланс: {account["balance"]}")
            return None
    print("Счет не найден!")
    return None


def expense_account(account_id, amount):
    data = get_data()
    for account in data:
        if account["id"] == account_id:
            account_balance = int(account["balance"])
            if amount > account_balance:
                print("Недостаточно средств на балансе")
                return None
            account_balance -= int(amount)
            account["balance"] = account_balance
            pull_data(data)
            print(
                f"Выполнен расход по балансу, Информация по счету: id: {account_id} name: {account["name"]}, "
                f"валюта:{account["currency"]}, баланс: {account["balance"]}")
            return None
    print("Счет не найден!")
    return None


def transfer_account(account_id, to_account_id, amount):
    data = get_data()
    for account in data:
        if account["id"] == account_id:
            account_balance = float(account["balance"])
            if amount > account_balance:
                print("Недостаточно средств на балансе")
                return None
            account_balance -= float(amount)
            account["balance"] = format(account_balance, '.2f')
            pull_data(data)
            print(
                f"Выполнен расход по балансу, Информация по счету: id: {account_id} name: {account["name"]}, "
                f"баланс: {account["balance"]} {account["currency"]}")

    data = get_data()
    for account in data:
        if account["id"] == to_account_id:
            if account["currency"] == "R":
                currency_now = float(asyncio.run(get_currency()))
                amount *= currency_now
                account_balance = float(account["balance"])
                account_balance += float(amount)
                account["balance"] = format(account_balance, '.2f')
                pull_data(data)
                print(f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                      f"баланс: {account["balance"]} {account["currency"]}")
                return None
            elif account["currency"] == "$":
                currency_now = asyncio.run(get_currency())
                amount /= float(currency_now)
                account_balance = float(account["balance"])
                account_balance += float(amount)
                account["balance"] = format(account_balance, '.2f')
                pull_data(data)
                print(f"Вы пополнили баланс Информация по счету: id: {account_id} name: {account["name"]}, "
                      f"баланс: {account["balance"]} {account["currency"]}")
                return None
    print("Счет не найден!")
    return None


def update_account(account_id):
    pass

