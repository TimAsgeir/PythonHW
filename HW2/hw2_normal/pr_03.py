'''
Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
в диапазоне от -100 до 100. В списке должно быть n - элементов.
Подсказка:
для получения случайного числа используйте функцию randint() модуля random
'''
import random

n = int(input('Введите число являющееся количеством элементов списка: ', ))

m = []

for i in range(n):
    m.append(random.randint(-100, 100))

print(m)