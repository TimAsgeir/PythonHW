'''
Задание-1:
Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
Первыми элементами ряда считать цифры 1 1
'''
def fib(n,m):
    def element(num):
        if (num == 1) | (num == 2):
            return 1
        else:
            return element(num - 1) + element(num - 2)

    series = []
    if m < n:
        pass
    elif m == n:
        series.append(element(n))
    else:
        series.append(element(n))
        series.append(element(n + 1))
        counter = m - n - 1
        idx = 2
        while counter > 0:
            series.append(series[idx - 1] + series[idx - 2])
            counter -= 1
            idx += 1
    return series
print(fib(1, 9))