import time
from functools import wraps
from utils.file_hendler import *


def format_time():
    current_time = time.time()
    local_time = time.localtime(current_time)

    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return formatted_time


def loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount=0):
    string_to_write = f"{time_now} | {type_operation} | {login} | {about_operation} "
    print(string_to_write)
    try:
        history = get_data_log(login)
        data = {
            "id": account_id,
            "amount": amount,
            "time": time_now,
            "type_operation": type_operation,
            "user": login,
            "about_operation": about_operation
        }
        history.append(data)
        pull_data_log(history, login)
    except FileNotFoundError:
        data = [
            {
                "id": account_id,
                "amount": amount,
                "time": time_now,
                "type_operation": type_operation,
                "user": login,
                "about_operation": about_operation
            }
        ]
        pull_data_log(data, login)


def loging_proces(time_now, type_operation, login, about_operation):
    string_to_write = f"{time_now} | {type_operation} | {login} | {about_operation} "
    print(string_to_write)
    try:
        history = get_data_log(login)
        data = {
            "time": time_now,
            "type_operation": type_operation,
            "user": login,
            "about_operation": about_operation
        }
        history.append(data)
        pull_data_log(history, login)
    except FileNotFoundError:
        data = [
            {
                "time": time_now,
                "type_operation": type_operation,
                "user": login,
                "about_operation": about_operation
            }
        ]
        pull_data_log(data, login)


def enter_user_log(func):
    @wraps(func)
    def wrapper(login, *arg):
        time_now = format_time()
        type_operation = "Вход в систему"
        about_operation = "Успешный вход в систему"
        result = func(login, *arg)
        if result == 1:
            loging_proces(time_now, type_operation, login, about_operation)
        else:
            return None
        return result
    return wrapper


def register_user_log(func):
    @wraps(func)
    def wrapper(login, *arg):
        time_now = format_time()
        type_operation = "Регистрация"
        about_operation = "Неудачная регистрация"
        result = func(login, *arg)
        if result:
            about_operation = "Успешная регистрация нового пользователя!"
            loging_proces(time_now, type_operation, login, about_operation)
        return result
    return wrapper


def crate_account_log(func):
    @wraps(func)
    def wrapper(login, currency, *arg):
        result = func(login, currency, *arg)
        time_now = format_time()
        account_id = result
        type_operation = f"Создание счета валюта: {currency}"
        about_operation = "Неудачная попытка создания счета"
        if result is None:
            loging_account_proces(time_now, type_operation, login, about_operation, account_id)
        else:
            about_operation = "Счет успешно создан!"
            loging_account_proces(time_now, type_operation, login, about_operation, account_id)
        return result
    return wrapper


def delete_account_log(func):
    @wraps(func)
    def wrapper(account_id, login, *arg):
        result = func(account_id, login, *arg)
        time_now = format_time()
        type_operation = f"Удаление счета"
        about_operation = "Неудачная попытка удаления"
        if result is True:
            about_operation = f"Счет: {account_id} успешно удален!"
            loging_account_proces(time_now, type_operation, login, about_operation, account_id)
        else:
            loging_account_proces(time_now, type_operation, login, about_operation, account_id)
        return result
    return wrapper


def transaction_income_log(func):
    @wraps(func)
    def wrapper(account_id, amount, login, *arg):
        result = func(account_id, amount, login, *arg)
        time_now = format_time()
        type_operation = f"Пополнение"
        about_operation = "Неудачная попытка пополнения"
        if result is True:
            about_operation = f"Счет: {account_id} на сумму: {amount} успешно пополнен!"
            loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount)
        else:
            loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount)
        return result
    return wrapper


def transaction_expense_log(func):
    @wraps(func)
    def wrapper(account_id, amount, login, *arg):
        result = func(account_id, amount, login, *arg)
        time_now = format_time()
        type_operation = f"Расходы"
        about_operation = "Неудачная попытка снятия"
        if result is True:
            about_operation = f"Счет: {account_id} на сумму: -{amount} успешно пополнен!"
            loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount)
        else:
            loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount)
        return result
    return wrapper


def transaction_transfer_log(func):
    @wraps(func)
    def wrapper(account_id, to_account_id, amount, login, *arg):
        result = func(account_id, to_account_id, amount, login, *arg)
        time_now = format_time()
        type_operation = f"Перевод"
        about_operation = "Неудачная попытка перевода"
        if result is True:
            about_operation = f"Выпеолнен успешный перевод со Счета: {account_id} на сумму: {amount}, на Счет: {to_account_id}!"
            loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount)
            loging_account_proces(time_now, type_operation, login, about_operation, to_account_id, amount)
        else:
            loging_account_proces(time_now, type_operation, login, about_operation, account_id, amount)
        return result
    return wrapper