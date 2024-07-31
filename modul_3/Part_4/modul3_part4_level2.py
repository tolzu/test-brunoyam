import json

print('Создайте логин и пароль')
login = input('Введите логин: ')
passwd = input('Введите пароль: ')

#account = {}
#with open('base.json', "w") as f:
#    json.dump(account, f)
def register(login, passwd):
    with open('base.json', "r") as f:
        base = json.load(f)
    if login not in base.keys():
        base[login] = passwd
        with open('base.json', "w") as f:
            json.dump(base, f)
    else:
        print('Логин уже существует!')
register(login, passwd)