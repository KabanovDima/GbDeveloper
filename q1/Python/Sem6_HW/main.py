import random
# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# some_list = []
# x1 = int(input('Введите первое число прогрессии: '))
# n = int(input('Введите разность: '))
# d = int(input('Введите количество элеиентов прогрессии: '))
# for i in range(d):
#     some_list.append(x1 + n * i)
# print(some_list)

# ////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)

n = int(input('Введите размер массива: '))
some_list = [random.randint(1,40) for _ in range(n)]
print(some_list)

x = int(input('Введите диапазон от: '))
y = int(input('Введите диапазон до: '))
print(some_list[x:y+1])