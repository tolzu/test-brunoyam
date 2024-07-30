import sys
sys.setrecursionlimit(1500)

def add_position(shopping_list):
    position = input('Введите название и количество')
    name, number = position.split()
    number = float(number)
    if name in shopping_list:
        shopping_list[name] += number
    else:
        shopping_list[name] = number
    return shopping_list

def remove_position(shopping_list):
    position = input('Введите название позиции, которую хотите удалить')
    shopping_list.pop(position, None)
    return shopping_list

def show_shopping_list(shopping_list):
    keys = sorted(shopping_list.keys())
    for key in keys:
        print(key, shopping_list[key])

def error():
    print('Я вас не понял, введите одну из команд: [добавить, удалить, показать, выход]')

def inputs(command):
    global shopping_list
    while True:
        command = input('Введите команду: ')
        if command == 'добавить':
            shopping_list = add_position(shopping_list)
#            print('Хотите ли еще добавить? Введите да или нет!')
            while True:
                enter = input('Хотите ли еще добавить? Введите да или нет! ')
                if enter == 'да':
                    shopping_list = add_position(shopping_list)
                elif enter == 'нет':
                    break
                else:
                    error()
        elif command == 'удалить':
            shopping_list = remove_position(shopping_list)
        elif command == 'показать':
            show_shopping_list(shopping_list)
        elif command == 'выход':
            break
        else:
            error()
#    return command

command = None
shopping_list = {}
inputs(command)
'''while True:
    command = input('Введите команду: ')
    if command == 'добавить':
        shopping_list = add_position(shopping_list)
    elif command == 'удалить':
        shopping_list = remove_position(shopping_list)
    elif command == 'показать':
        show_shopping_list(shopping_list)
    elif command == 'выход':
        break
    else:
        error()
'''