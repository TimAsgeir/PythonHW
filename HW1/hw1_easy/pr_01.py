'''
Задача-1: Дано произвольное целое число (число заранее неизвестно).
Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
Подсказки:
* постарайтесь решить задачу с применением арифметики и цикла while;
* при желании решите задачу с применением цикла for.
'''

'''
number = input('Введите любое целое число: ')
while number > 0:
    print(number % 10)
    number //= 10
'''
number = input("Введите любое целое число: ")
for num in number:
    print(num)