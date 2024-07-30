a = int(input('Введите длину стороны a: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))
#p = (a + b + c) / 2

def area(a, b, c):
    p = (a + b + c) / 2
    sqrt = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    print(sqrt)

area(a, b, c)