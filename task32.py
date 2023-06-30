# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = int(input('Задайте размер списка '))
min_num = int(input('Задайте минимальную границу диапазона '))
max_num = int(input('Задайте максимальную границу диапазона '))
lst = [randint(1,10) for _ in range(n)]
result = [i for i in range(len(lst)) if min_num <= lst[i] <= max_num]
print(f'Список: {lst}\nИндексы элементов, принадлежащих диапазону от {min_num} до {max_num}:', end=' ')
print(*result)