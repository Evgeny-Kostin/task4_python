# Задача 30:  Заполните список элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#my_list=list()
# a1=int(input('Введите первый элемент: '))
# d = int (input('Введите разность: '))
# n = int (input('Введите колличество элементов: '))
# for i in range(n):
#     an = a1 + i * d
#     #list_1=list(an) как полученные значения закинуть в список?
#     print(an)

# Задача 32: Определить индексы элементов списка, значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# new_list = []
# max = 100
# min = -91
# for i in range(len(my_list)):
#     if min <= my_list[i] <= max:
#         print(i, end=' ')