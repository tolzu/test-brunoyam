x = int(input('Введите начальную сумму вклада: '))
p = int(input('Введите годовую процентную ставку: '))
y = int(input('Введите конечную сумму вклада: '))
years = 0
while x < y:
    x = int(x * (1 + (p / 100)))
    years += 1
    print(x)
if years < 0:
    years == 0
    print(years)
else:
    print(years - 1)