'''
Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
1. Сколько слов в тексте?
2. Сколько букв английского алфавита в тексте?
'''

import string

s = input("Введите текст: ")

sl = sw = s

for i in string.punctuation:
    sw = sw.replace(i, "")

sw = sw.strip()

while "  " in sw:
    sw = sw.replace("  ", " ")

w = sw.split(" ")

print(len(w))

count = dict()

for word in w:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

for i in sl:
    if i not in string.ascii_letters:
        sl = sl.replace(i, "")

print(len(sl))