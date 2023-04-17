#!/usr/bin/python3

x = input('Введите число 1:\n')
y = input('Введите число 2:\n')

max1 = (x > y) * x + (y >= x) * y
print('Max: ', max1)
