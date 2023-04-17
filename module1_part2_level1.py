#!/usr/bin/python3

x = int(input('Введите целое число 1:\n'))
y = int(input('Введите целое число 2:\n'))
z = int(input('Введите целое число 3:\n'))

if x == y and x == z:
    print('3')
elif (x == y and x != z) or (x != y and x == z) or (x != y and y == z):
    print('2')
else:
    print('0')
