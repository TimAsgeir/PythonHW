'''
Даны два произвольные списка.
Удалите из первого списка элементы, присутствующие во втором списке.
'''
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [2, 4, 6, 8]

c = []

for i in a:
    if i not in b:
        c.append(i)

print(c)