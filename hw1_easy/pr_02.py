'''
Задача-2: Исходные значения двух переменных запросить у пользователя.
Поменять значения переменных местами. Вывести новые значения на экран.
Подсказка:
* постарайтесь сделать решение через дополнительную переменную
или через арифметические действия
Не нужно решать задачу так:
print("a = ", b, "b = ", a) - это неправильное решение!
'''
first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')

number = first_num
first_num = second_num
second_num = number
print('Первое число: ', first_num)
print('Второе число: ', second_num)