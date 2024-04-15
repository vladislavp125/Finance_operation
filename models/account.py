import csv
from services.account_management import get_balance_


class Accaunt:
    def __init__(self, user_id, name, currency):
        self.account_id = user_id
        self.name = name
        self.currency = currency
        self.balance = 0

    def add_income(self, amount):
        pass

    def add_expense(self, amount):
        pass

    def get_balance(self):
        self.balance = get_balance_(self.account_id, self.name)
        return self.balance

    def transfer(self, other_account, amount):
        pass

