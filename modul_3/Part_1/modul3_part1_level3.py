num = input('Введите целое число: ')

results = []
for i in range(0, len(num), 1):
    results.append(int(num[i: i + 1]))
#print(results)
total = 0
for result in results:
    total += result
print(total)