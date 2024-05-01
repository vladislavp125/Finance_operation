import json


def pull_data(data):
    with open("data/accounts/user_account.json", "w", encoding='utf8') as file:
        json.dump(data, file, indent=3)


def get_data():
    with open("data/accounts/user_account.json", encoding='utf8') as file:
        data = json.load(file)
    return data


def get_data_log(login):
    with open(f"data/transactions/{login}_logs.json", encoding='utf8') as file:
        data = json.load(file)
        return data



def pull_data_log(data, login):
    with open(f"data/transactions/{login}_logs.json", "w", encoding='utf8') as file:
        json.dump(data, file, indent=3)


