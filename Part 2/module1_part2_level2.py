#!/usr/bin/python3

x1 = int(input('Введите целое число от 1 до 8\n'))
y1 = int(input('Введите целое число от 1 до 8\n'))
x2 = int(input('Введите целое число от 1 до 8\n'))
y2 = int(input('Введите целое число от 1 до 8\n'))

if (abs(x1 - x2) == 0) or (abs(y1 - y2) == 0):
    print('YES')
else:
    print('NO')
