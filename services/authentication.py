from utils.logger import *
import json


def file_check_pass(login):
    with open("data/users_data.json") as file:
        data = json.load(file)
        for user in data:
            if user["login"] == login:
                return user["password"]
        return None


def hash_pass(password):
    h = 0
    hh = 1
    num = 1234
    for i in str(password):
        h += ord(i)
        hh *= ord(i)
    h = h % num
    hh = hh % num
    return str(h) + str(hh)


def pass_try(login, password):
    password_old = file_check_pass(login)
    if password_old is None:
        return None
    if hash_pass(password) == str(password_old):
        return True


@enter_user
def log_in(login, password):
    try:
        if pass_try(login, password):
            auth = 1
            print("Вы успешно авторизовались")
            return auth
        else:
            print("Не верный логин или пароль!")
            print("Вы можете зарегистрироваться написав 'Рег'")
    except FileNotFoundError:
        print("Не верный логин или пароль!")
        print("Вы можете зарегистрироваться написав 'Рег'")


def logout(auth):
    auth -= 1
    return auth


def register(login, password, email):
    password_h = hash_pass(str(password))
    try:
        with open("data/users_data.json", encoding='utf8') as f:
            data = json.load(f)
            for user in data:
                if user["login"] == login:
                    print("Логин, уже занят, придумайте другой")
                    return None
                else:
                    continue
            with open("data/users_data.json", "w", encoding='utf8') as f_w:
                new_user = {f"login": login, "password": password_h, "email": email}
                data.append(new_user)
                json.dump(data, f_w, indent=3)
                print("Аккаунт успешно зарегистрирован!")
                return new_user
    except FileNotFoundError:
        with open("data/users_data.json", "w") as f:
            new_user = [{f"login": login, "password": password_h, "email": email}]
            json.dump(new_user, f, indent=3)

# register(123, 123, "vladislavp")
# register("ffff", 123, "vladislavp")
# log_in("ffff", 123)
