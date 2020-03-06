'''
Задание-1:
Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу
'''
num = int(input("Введите число: "))
simple = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        simple = False
        break
if simple:
    print("Простое")
else:
    print("Не простое")