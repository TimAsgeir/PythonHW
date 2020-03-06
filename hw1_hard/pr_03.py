'''
Задание-3
Вывести на экран:
AAABBBAAABBBAAABBB
BBBAAABBBAAABBBAAA
AAABBBAAABBBAAABBB
(таких строк n, в каждой строке m троек AAA)
'''
a = "AAABBB"
b = "BBBAAA"

n = int(input("Введите n: "))
m = int(input("Введите m: "))

for i in range(n):
    for j in range(m):
        print(a, end="")
    print()
    a,b = b, a
