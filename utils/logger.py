import time
from functools import wraps
from utils.file_hendler import *

#[Дата и время] | [Тип операции] | [Пользователь] | [Описание операции]


def format_time():
    current_time = time.time()
    local_time = time.localtime(current_time)

    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return formatted_time



def enter_user(func):
    @wraps(func)
    def wrapper(login, *arg):
        time_now = format_time()
        type_operation = "Вход в систему"
        about_operation = "Успешный вход в систему"
        result = func(login, *arg)
        if result == 1:
            string_to_write = f"{time_now} | {type_operation} | {login} | {about_operation} "
            print(string_to_write)
            try:
                history = get_data_log(login)
                data = {"time": time_now, "type_operation": type_operation, "user": login, "about_operation": about_operation}
                history.append(data)
                pull_data_log(history, login)
            except FileNotFoundError:
                data = [{"time": time_now, "type_operation": type_operation, "user": login, "about_operation": about_operation}]
                pull_data_log(data, login)
        return result
    return wrapper


#####################
def registr_user_log(func):
    @wraps(func)
    def wrapper(login, *arg):
        time_now = format_time()
        type_operation = "Вход в систему"
        about_operation = "Успешный вход в систему"
        result = func(login, *arg)
        if result == 1:
            string_to_write = f"{time_now} | {type_operation} | {login} | {about_operation} "
            print(string_to_write)
            try:
                history = get_data_log(login)
                data = {"time": time_now, "type_operation": type_operation, "user": login,
                        "about_operation": about_operation}
                history.append(data)
                pull_data_log(history, login)
            except FileNotFoundError:
                data = [{"time": time_now, "type_operation": type_operation, "user": login,
                         "about_operation": about_operation}]
                pull_data_log(data, login)
        return result
    return wrapper



