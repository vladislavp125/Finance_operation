from utils.file_hendler import *
from models.account import Accaunt
import random
import json


def add_transaction(account_id, amount, transaction_type, login):
    if transaction_type == "1": #"Income"
        account = Accaunt(login)
        account.add_income(account_id, amount)

    elif transaction_type == "2": #"Expense"
        account = Accaunt(login)
        account.add_expense(account_id, amount)

    elif transaction_type == "3": #"transfer"
        to_account_id = int(input("Введите id счета на который хотите перевести деньги: "))
        account = Accaunt(login)
        account.transfer(account_id, to_account_id, amount)


def get_transactions(account_id, start_date, end_date):
    pass

