import csv
from services import authentication


class User:
    def __init__(self, login, password, email=None):
        self.username = login
        self.password = password
        self.email = email
        self.auth = None

    def register(self):
        authentication.register(self.username, self.password, self.email)
        self.auth = 1

    def login(self):
        self.auth = authentication.log_in(self.username, self.password)

    def update_profile(self):
        pass