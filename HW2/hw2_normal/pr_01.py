'''
Задача-1:
Дан список, заполненный произвольными целыми числами, получите новый список,
элементами которого будут квадратные корни элементов исходного списка,
но только если результаты извлечения корня не имеют десятичной части и
если такой корень вообще можно извлечь
Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]
'''
'''
# Пример со случайным списком в периоде от -100 до 100
import random

a = []

for i in range(20):
    a.append(random.randint(-100, 100))
    
#print(a)

b = []

for i in a:
    if i > 0 and i ** 0.5 % 1 == 0:
        b.append(int(i ** 0.5))

print('Новый список: ', b)
'''
import random

a = [2, -5, 8, 9, -25, 25, 4]
b = []

for i in a:
    if i > 0 and i ** 0.5 % 1 == 0:
        b.append(int(i ** 0.5))

print('Новый список: ', b)