# 1
'''Создайте функцию которая которая берёт лист делит его пополам и обе стороны разворачивает в противоположную сторону. Пример:
Оригинальный Лист:
list_1 = ['name', 'age', '1', '19']
Изменённый Лист:
list_1 = ['age', 'name', '19', '1']'''

# list_1 = ['name', 'age', '1', '19']
# def half_reversed(value):
#     first_part = value[:(len(value)//2)][::-1]
#     second_part = value[len(value)//2:][::-1]
#     return first_part + second_part
# print(half_reversed(list_1))

# 2
'''Создайте с помощью рекурсии функцию которая генерирует 10 чисел Фибоначчи:
1,1,2,3,5,8,13,21,34,...'''
# def fibonachi(n):
#     a,b = 1, 1
#     for i in range(n):
#         yield a
#         a,b = b, a+b

# data = list(fibonachi(10))
# print(data)

# 3
'''Создайте функцию сложения, затем функцию вычитания двух чисел...
Создайте 3-ю функцию которая вызывает первые 2 внутри себя.'''

# def sloj_vych():
#     def vnutri_sebya(a,b):
#         c = a+b
#         d = a-b
#         return (c,d)
#     print(vnutri_sebya(6,9))
# sloj_vych()

# 4
'''Спросите у пользователя имя файла. Создайте функцию которая создаёт файл с именем которое передал пользователь. Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную.
'''

# name_of_file = input("Название файла: ")

# def create_file(name_file):
#     f = open(name_file, 'w')
#     f.close()

# test = create_file(name_of_file)

# 5
'''Представьте Вы работаете в Мобильной Компании и вас попросили создать генератор номеров.
Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0444 _ _ _ _ _ _.
Номера которые вы можете генерировать могут содержать в себе только числа 145790. 
Пример: 0444150971 0444111777 0444457901'''

# from random import choice

# def gen_number():
#     allow_nums = '145790'
#     res_nums = '0444'
#     for i in range(6):
#         res_nums += choice(allow_nums)
#     return res_nums

# print(gen_number())

# 6
'''Напишите программу которая выводит только нечётные числа с помощью рекурсии
'''
# def print_odd_nums(n):
#     print(n)
#     if n < 1:
#         return None
#     if n % 2 == 0:
#         return print_odd_nums(n - 2)
#     else:
#         return print_odd_nums(n - 1)

# print(print_odd_nums(7))

# 7
'''Напишите функцию которая принимает SET и рекурсивно
удаляет оттуда по одному элементу при запуске.
'''
# my_nums = {1, 2, 3, 4, 5}
# def del_set_item(user_nums):
#     my_nums.pop()
#     return my_nums

# print(my_nums)
# print(del_set_item(my_nums))
# print(del_set_item(my_nums))
# print(del_set_item(my_nums))

