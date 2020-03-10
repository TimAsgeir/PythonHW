'''
Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра
'''
import string

text_1 = input('Введите текст 1: ', )
text_2 = input('Введите текст 2: ', )

text = []

for i in string.punctuation:
    text_1 = text_1.replace(i, "")

text_1 = text_1.strip()

text_1 = text_1.lower()

while "  " in text_1:
    text_1 = text_1.replace("  ", " ")

words_1 = text_1.split(" ")

for i in string.punctuation:
    text_2 = text_2.replace(i, "")

text_2 = text_2.strip()

text_2 = text_2.lower()

while "  " in text_2:
    text_2 = text_2.replace("  ", " ")

words_2 = text_2.split(" ")

print(set(words_1).intersection(set(words_2)))