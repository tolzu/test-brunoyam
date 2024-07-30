l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
l_final = []
for i in l:
    if l.count(i) > 1 and i not in l_final:
        l_final.append(i)
print(l_final)