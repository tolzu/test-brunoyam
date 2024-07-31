import json

print('Создайте логин и пароль')
login = input('Введите логин: ')
passwd = input('Введите пароль: ')

account = {}
def register(login, passwd):
    account[login] = passwd
    with open('base.json', "w") as new_login:
        json.dump(account, new_login)

register(login, passwd)