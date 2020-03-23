'''
Задание-2:
Дан шестизначный номер билета. Определить, является ли билет счастливым.
Решение реализовать в виде функции.
Билет считается счастливым, если сумма его первых и последних цифр равны.
!!!P.S.: функция не должна НИЧЕГО print'ить
'''
def tlucky(tnumber):
    num = str(tnumber)
    sum_1 = int(num[:1]) + int(num[1:2])
    sum_2 = int(num[-1]) +int(num[-2])
    if sum_1 == sum_2:
        return True
    else:
        return False

tnumber = 2215421
print('Билет счастливый? ', tlucky(tnumber))