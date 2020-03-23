'''
Задача-2:
Напишите функцию, сортирующую принимаемый список по возрастанию.
Для сортировки используйте любой алгоритм (например пузырьковый).
Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
'''
li = [5,2,7,4,0,9,8,6]

def sort_to_max(origin_list):
    n = 1
    length_array = len(origin_list)
    while n < length_array:
        for i in range(length_array-n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
        n += 1

lis = [4, 12, -16, 1.2, 40, -19, 3, 3, 0]
sort_to_max(lis)
print(lis)