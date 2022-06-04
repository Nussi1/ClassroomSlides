# 1
'''Внутри my_module.py создайте вызваннную print которая выводит текст "Я функция из my_module.py". А затем импортируйте my_module.py в другой файл.
'''

print('Я функция из my_module.py')

# 2
'''Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] и вытащите 4 рандомных имени оттуда и сохраните в другой список.'''

# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# names2 = []

# for i in range(4):
#     names2.append(random.choice(names))
# print(names2)

# 3
'''Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.'''

# import sys

# print(sys.platform)

# 4
'''Через терминал передайте Python несколько аргументов, а затем выведите их на экран.'''

# import sys
# text = sys.stdin.readline()
# sys.stdout.write(text)

# 5
'''Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов.'''

# from random import randint
# from os import system


# for i in range(5):
#     r = r(1,10)
#     system(f'touch /Users/nuraim/Desktop/{r}.txt')

# 6
'''Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.'''

# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

# com1 = []
# com2 = []
# com3 = []
# com4 = []
# count = 1
# len_com = len(names)//4
# while names != []:
#     name = random.choice(names)
#     if count <= len_com:
#         com1.append(name)
#         names.remove(name)
#     elif count <= len_com*2:
#         com2.append(name)
#         names.remove(name)
#     elif count <= len_com*3:
#         com3.append(name)
#         names.remove(name)
#     else:
#         com4.append(name)
#         names.remove(name)
#     count+=1
# print(com1)
# print(com2)
# print(com3)
# print(com4)

# 7
'''Напишите программу которая будет принимать аргументы sys.argv и выводить на экран оттуда всё что передал пользователь.'''

# import sys
# print("1-Аргумент", "2-Аргумент", sys.argv[0])

# 8
'''Спросите у пользователя 2 значения через input() а затем через модуль sys проверьте какое из 2-х значений занимает больше памяти.'''

# import sys
# f_val, s_val = input("First value: "), input("Second value: ")
# if sys.getsizeof(f_val) > sys.getsizeof(s_val):
#     print("First value is bigger")
# else:
#     print("Second value is bigger")

# 9
'''Создайте программу которая спрашивает у пользователя число N для генерации пароля а затем генерирует ему пароль длиною N символов.'''

# import random
# import string
# def generate_random_symbols(len_of_char):
#     letters = string.ascii_lowercase
#     rand_symbols = ''.join(random.choice(letters) for i in range(len_of_char))
#     return rand_symbols
# n = int(input("input n: "))
# print(generate_random_symbols(n))

# 10
'''Создайте игру Камень-Ножницы-Бумага с Компьютером. Где компьютер даёт вам выбрать опцию, а сам затем генерирует своё значение. По итогу говорит выиграли вы, проиграли или ничья.'''

# from random import randint
# my_list = ['0.Камень', '1.Ножницы', '2.Бумага']
# for i in my_list: print(i)
# x, ran_x = int(input("Выберите номер опции: ")), randint(0, len(my_list)-1)
# if x == 0 and ran_x == 0 or x == 1 and ran_x == 1 or x == 2 and ran_x == 2:
#     print("ничья")
# elif x == 0 and ran_x == 1 or x == 1 and ran_x == 2 or x == 2 and ran_x == 0:
#     print("Вы выиграли")
# else:
#     print("Вы проиграли")

# 11
'''Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12. Также получите число кратное пяти в пределах от 5 до 100.'''
# from random import randrange
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))

# 12
'''Найдите модуль os и sys в google и поработайте с каждым отдельно
'''
# import os, sys
# print(os.name)
# print(sys.exc_info)

# 13
'''Определить дату, которая наступит через 1000 дней от текущей даты
'''
# import datetime
# dt = datetime.datetime.now()
# thdt = datetime.timedelta(days=1000)
# print(dt+thdt)


# 1
'''С помощью цикла пройдите по листу numbers и выводите на экран сумму двух соседних чисел.'''
# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# i, j = 0, 1
# while j != len(numbers)-1:
#     print(numbers[i] + numbers[j])
#     i += 1
#     j += 1


# 2
'''В Python есть модуль datetime а в модуле есть особенные функции которые показывают настоящее время. С помощью модуля datetime выведите на экран сколько времени в данный момент.'''
# import datetime
# print(datetime.datetime.now())


# 3
'''В Python есть модуль time, с помощью него можно отправлять программу в СОН.
Запустите цикл for i in range(10) и каждый шаг цикла вызывайте функцию модуля time которая заставляет программу ЗАСНУТЬ.'''
# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)


# 4
'''В Python есть ВСТРОЕННАЯ функция которая позволяет объединять ДВА списка для цикла for.
Запустите цикл for с двумя переменными которые будут проходить по list1 и list2
одновременно и выводите эти переменные на экран.'''
# list1 = [1,3,5,7,9,11,13]
# list2 = [2,4,6,8,10,12,14]
# for i, j in zip(list1, list2):
#     print(i, j)