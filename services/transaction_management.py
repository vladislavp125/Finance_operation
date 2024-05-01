from utils.file_handler import *
from models.account import Accaunt
import random
import json
import time
import datetime as DT


def add_transaction(account_id, amount, transaction_type, login):
    if transaction_type == "1": #"Income"
        account = Accaunt(login)
        account.add_income(account_id, amount)

    elif transaction_type == "2": #"Expense"
        account = Accaunt(login)
        account.add_expense(account_id, amount)

    elif transaction_type == "3": #"transfer"
        to_account_id = input("Введите id счета на который хотите перевести деньги: ")
        account = Accaunt(login)
        account.transfer(account_id, to_account_id, amount)


def get_transactions(login, account_id, start_date, end_date):
    data = get_data_log(login)
    data_out = []
    for log in data:
        if "id" in log:
            if int(log["id"]) == int(account_id):
                if time_chek(start_date) <= time_chek(log["time"]) <= time_chek(end_date):
                    data_out.append(log)
                    continue
    for log in data_out:
        print(f"{log["time"]} | {log["type_operation"]} | {log["user"]} | {log["about_operation"]}")
    total_income = 0
    total_expense = 0
    for log in data_out:
        if log["type_operation"] == "Пополнение":
            total_income += int(log["amount"])
    for log in data_out:
        if log["type_operation"] == "Расходы":
            total_expense -= int(log["amount"])
    final_balance = total_income + total_expense
    report = (
        f"Общий доход: {total_income}\n"
        f"Общий расход: {total_expense}\n"
        f"Конечный баланс: {final_balance}"
    )
    print(report)


def get_history_transactions(login, account_id):
    data = get_data_log(login)

    data_out = []
    for log in data:
        if "id" in log:
            if int(log["id"]) == int(account_id):
                data_out.append(log)

    for log in data_out:
        print(f"{log["time"]} | {log["type_operation"]} | {log["user"]} | {log["about_operation"]}")


def time_chek(date):
    dt = DT.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return dt.timestamp()


