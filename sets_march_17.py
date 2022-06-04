# 0
'''Из множества 
№ 1 - удалите все числа 6.'''

# from cgitb import reset

# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(6)
# print(dates_of_birth)

# 1
'''Создайте SET состоящий из 3 вложенных SET.'''

# a = frozenset({1, 2, 3})
# b = frozenset({4, 5, 6})
# c = frozenset({9, 8, 7})
# result = set([a, b, c])
# print(result)

# 2
'''Во множестве №3 найдите объекты которых нет во множестве №2'''

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_2.difference(farm_1))

# 3
'''Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
А затем удалите через .pop() элемент и посмотрите что же вы удалили.'''

# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)
# my_set.pop()
# print(my_set)

# 4
'''Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
Сделайте так чтобы эти данные уже никто не смог поменять позже.'''

# my_new_list = []
# for i in range(10):
#     x = int(input('Введите значение: '))
#     my_new_list.append(x)

# my_frozen_set = frozenset(my_new_list)
# print(my_frozen_set)

# 5
'''Из Множество 2 и 3 
Напишите код, который: Выведет новое множество, которое есть как в
первой ферме, так и во второй.

Выведет новое МНОЖЕСТВО, состоящее из животных,
которые есть в первой ферме, но нет во второй.
'''

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# res_farm = farm_1.intersection(farm_2)
# print(res_farm)

# print(farm_1.difference(farm_2))