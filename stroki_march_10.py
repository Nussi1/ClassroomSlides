# 1
# Взять строку №1 и посчитать сколько там слов.

# t = 'Google sozdast specialnuyu komandu dlya poiska bagov v osobo vazhnyh prilozheniyah'
# word_list = t.split()
# number_of_words = len(word_list)
# print(number_of_words)

# 2
'''Взять строку №8 и поделить её по пробелам и узнать тип данных каждого слова.'''

# stroka_8 = "u vas est stroka 'Zapusk Ethereum 2.0 sostoitsya 1 december. Na deposit contract vneseno more than 524 288 ETH'"
# stroka_8 = stroka_8.split(' ')
# my_list = []
# for i in stroka_8:
#     try:
#         my_list.append(float(i))
#     except:
#         my_list.append(i)
#
# for i in my_list:
#     print(type(i))

# 3
''' Взять строку №3 и сделать каждое её слово с большой буквы.
Строка №3: хакеры слили в сеть данные пакистанской энергетической компании k-Electric'''

# text_3 = 'Хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
# print(text_3.upper())

# 4
'''Спросить у пользователя символ и поделить строку №4 по этому символу.'''

# stroka = 'GitHub'
# print(stroka.strip(input('vvedite lyubuyu bukvu ot slova github: ')))


# 5
'''Взять строку №5 и заменить все буквы Е на число 3.'''

# stroka_5 = 'Botnet IPStorm, v kotoryi ranee vhodil lish Windows-maschine, uvelichilsya do 13 500 zarazhennyh sistem'
# print(stroka_5.replace('e', '3'))

# 6

'''Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом.'''

# txt6 = 'Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом'
# first_part = txt6[0:int(len(txt6)/2)]
# second_part = txt6[int(len(txt6)/2) : len(txt6)-1]
# print(first_part.lower() + second_part.upper())

# 7
'''Сделать из булева значения True  - строку.'''

# txt7 = True
# print(str(txt7))