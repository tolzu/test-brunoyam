#!/usr/bin/python3

while True:
    print('Введите пароль который должен состоять не менее чем из 8 символов включая заглавные и прописные буквы')
    psw = input()
    if (len(psw) > 8) and (not psw.islower() and not psw.isupper() and not psw.isdigit()):
        print('Пароль соответствует')
    else:
        print('Пароль не соответствует заданным критериям!')
