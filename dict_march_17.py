# 1
'''Из Dictionary №1:
Добавьте в меню
напитки как ключ "drinks",

А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.'''

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)

# 2
'''Создайте пустой словарь.

Запустите цикл который 3 раза спросит его имя и его пароль.

Записывайте имя пользователя как ключ, а пароль как его значение.'''

# my_dict2 = {}
# for i in range(3):
#     name = input('Input your name: ')
#     password = input('')
#     my_dict2[name] = password

# 3
'''Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
С помощь цикла for пройти вывести на экран строку:
"Здравствуйте <Имя>  Прекрасная профессия <Профессия>"'''
# my_dict3 = {}
# spisok = {'Marat': 'IT-specilist',
# 	'Aida': 'Manager',
# 	'Nuraiym': 'DataScientist',
# 	'Malika': 'Doctor'}
# for key, value in spisok.items():
#     print('Hello, ', key, 'Excellent profession ', value)

# 4
'''Из Dictionary №1:
Добавьте в меню 
 'besh_barmak' который стоит  130 сом.
Оказалось лагман слишком дешевый. Обновите цену на 135
Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
Удалить borsh'''

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = '130 som'
# menu['besh_barmak'] = '135 som'
# menu.pop('borsh')
# print(menu)

# 5
'''Есть список Южноамериканских стран
СПИСОК №2
в котором Суринам встречается два раза. Необходимо написать программу,
которая удалит дублирующуюся запись, и возвратит в результате словарь {'номер': 'страна'}.'''
 
# south_american_countries = [
#     'Argentina', 'Bolivia', 'Brazil',
#     'Chile', 'Colombia', 'Ecuador',
#     'Guyana', 'Paraguay', 'Peru',
#     'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

# new_dictionary = {}

# cnt = 1
# for i in set(south_american_countries):
#     new_dictionary[cnt] = i
#     cnt += 1
# print(new_dictionary)