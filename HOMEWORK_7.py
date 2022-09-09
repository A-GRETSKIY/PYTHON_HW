            # 1.Используя словарь, напишите программу, которая выведет на экран
            # название дня недели по его номеру. (1 - «Monday»)

week_day = int(input())
days = {1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
        }
res = days.get(week_day, 'Error')   # если в словаре нету элемента, то get возвращает None, но его можно поменять
print(res)

            # 2.Представьте описание кота (домашнее животное) на основе словаря

cat = {
    'name': 'Tom',
    'color': 'black',
    'age': '2',
    'breed': 'Sphynx',
    }
print(cat['name'])
print(cat)

            # 3.Напишите программу которая считает строку текста с клавиатуры и
            # выведет на экран статистику, сколько раз какая буква встречается в
            # этой строке. Например, для строки «Hello world» эта статистика
            # выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д.

            # Exemple 1

s = input()
res = {}
for item in s:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1
print(res)

            # Exemple 2

s = input()
res = {}
for item in s:
    if not res.get(item):
        res[item] = s.count(item)
print(res)

            # 4.Ввести с клавиатуры число (до миллиона), которое обозначает количество
            # долларов и центов пользователя. Вывести это количество прописью.
            # Например:
            # How much money do you have?
            # 123,34
            # You have: one hundred twenty three dollars thirty four cents


            # 5.Напишите программу, которая переведет целое число (от 1 до 100) из
            # римской записи в обычные цифры.
            # Например: XXII -> 22
            
             # 1.Используя словарь, напишите программу, которая выведет на экран
            # название дня недели по его номеру. (1 - «Monday»)

week_day = int(input())
days = {1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
        }
res = days.get(week_day, 'Error')   # если в словаре нету элемента, то get возвращает None, но его можно поменять
print(res)

            # 2.Представьте описание кота (домашнее животное) на основе словаря

cat = {
    'name': 'Tom',
    'color': 'black',
    'age': 2,
    'breed': 'Sphynx',
    }
print(cat['name'])
print(cat)

            # 3.Напишите программу которая считает строку текста с клавиатуры и
            # выведет на экран статистику, сколько раз какая буква встречается в
            # этой строке. Например, для строки «Hello world» эта статистика
            # выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д.

            # Exemple 1

s = input()
res = {}
for item in s:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1
print(res)

            # Exemple 2 (УПРОЩЕННЫЙ И БОЛЕЕ БЫСТРЫЙ ВАРИАНТ ПРЕДЫДУЩЕГО)

s = input()
res = {}
for item in s:
    if not res.get(item): # ЕСЛИ МЕТОД GET = FALSE, ТО -> res[item] = s.count(item)
        res[item] = s.count(item)
print(res)

            # Exemple 3 - ЧЕРЕЗ МНОЖЕСТВА (SET) - РАБОТАЕТ БЫСТРЕЕ

s = input()
res = {}
for item in set(s):
    if not res.get(item):
        res[item] = s.count(item)
print(res)

            # 4.Ввести с клавиатуры число (до миллиона), которое обозначает количество
            # долларов и центов пользователя. Вывести это количество прописью.
            # Например:
            # How much money do you have?
            # 123,34
            # You have: one hundred twenty three dollars thirty four cents


            # 5.Напишите программу, которая переведет целое число (от 1 до 100) из
            # римской записи в обычные цифры.
            # Например: XXII -> 22

rome_numbers = (('C', 100),
                ('XC', 90),
                ('L', 50),
                ('XL', 40),
                ('X', 10),
                ('IX', 9),
                ('V', 5),
                ('IV', 4),
                ('I', 1)
                )
s = input()
result = 0
index = 0
for numeral, integer in rome_numbers:
    while s[index:index + len(numeral)] == numeral:
        index += len(numeral)
        result += integer
print(result)    

