
import json


def file_check(login):
    with open("data/users_data.json", "r") as file:
        data_ = json.load(file)
        username = "login_" + str(login)
        for user_data in data_:
            if username in user_data:
                return False
        return True


def file_check_pass(login):
    with open("data/users_data.json", "r") as file:
        data_ = json.load(file)
        username = "login_" + str(login)
        for user_data in data_:
            if username in user_data:
                return user_data[username][0]["password"]
        return None


def hash_pass(password):
    h = 0
    hh = 1
    num = 1234
    for i in password:
        h += ord(i)
        hh *= ord(i)
    h = h % num
    hh = hh % num
    return str(h) + str(hh)


def pass_try(login, password):
    try:
        user_d = file_check_pass(login)
        password_old = user_d
        if hash_pass(password) == str(password_old):
            return True
    except FileNotFoundError:
        print("Файл с таким логином не найден")
        print()
        print("Вы можете зарегистрироваться написав 'Рег'")


def log_in(login, password):
    if pass_try(login, password):
        auth = 1
        return auth
    else:
        print("Не верный логин или пароль!")
        print("Вы можете зарегистрироваться написав 'Рег'")


def add_js_file(data):
    with open("data/users_data.json", 'r') as file:
        data_op = json.load(file)
        data_op.append(data)
    with open("data/users_data.json", 'w') as file:
        json.dump(data_op, file, indent=3)


def logout(auth):
    auth -= 1
    return auth


def register(login, password, email):
    password_h = hash_pass(password)
    data = {f'login_{login}': [{"password": password_h, "email": email}]}
    try:
        if file_check(login):
            add_js_file(data)
            return data
        else:
            print('Аккаунт с таким логином уже зарегистрирован')
    except FileNotFoundError:
        with open("data/users_data.json", 'a') as file:
            json.dump([data], file, indent=3)
            print([data])
        return data


#while True:
#    o = str(input("operation"))
#    if o == "1":
#        login = input("Введите логин: ")
#        password = input("Придумайте пароль: ")
#        email = input("Укажите email: ")
#        register(login, password, email)
#    elif o == "2":
#        login = str(input("Введите логин: "))
#        password = str(input("Придумайте пароль: "))
#        data = str(log_in(login, password))
#        print(data)
#
#
#