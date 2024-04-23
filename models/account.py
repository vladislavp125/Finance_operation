import csv
from services.account_management import *
from random import randint


class Accaunt:
    def __init__(self, user_login, name=None, currency=None):
        self.user = user_login
        self.name = name
        self.currency = currency

    def create_account(self):
        create_account(self.user, self.name, self.currency)

    def add_income(self, account_id, amount):
        income_account(account_id, amount)

    def add_expense(self, account_id, amount):
        expense_account(account_id, amount)

    def transfer(self, account_id, other_account, amount):
        transfer_account(account_id, other_account, amount)

    def delete_account(self, account_id):
        delete_account(account_id)
