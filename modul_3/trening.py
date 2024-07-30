
number = 0
def increment():
    global number
    if number < 3:
        number += 1
increment()
increment()
increment()
increment()
print(number)