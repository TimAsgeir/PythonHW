'''
Задача-1:
Дан список фруктов.
Напишите программу, выводящую фрукты в виде нумерованного списка,
выровненного по правой стороне.
Пример:
Дано: ["яблоко", "банан", "киви", "арбуз"]
Вывод:
1. яблоко
2.  банан
3.   киви
4.  арбуз
Подсказка: воспользоваться f-строками
'''
m = ["яблоко", "банан", "киви", "арбуз"]

max_len = 0
for i in m:
    if len(i) > max_len:
        max_len = len(i)

for num, i in enumerate(m, start=1):
    print(f"{num}. {i:>{max_len}}")