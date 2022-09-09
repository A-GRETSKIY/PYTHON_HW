            # 1. Напишите программу, которая посчитает сколько букв «b» в введенной
            # строке текста.

x = input()
print(x.count('b'))

            # 2. Считайте строку, которая будет представлять имя человека, введенное с
            # клавиатуры. Проверьте эту строку на валидность. Имеется в виду, что
            # например, в имени человека не может быть цифр, оно должно
            # начинаться с большой буквы, за которой должны следовать маленькие.

name = input('Name: ')
res = 'Correct' if name.istitle() and name.isalpha() else 'Incorrect'
print(res)

            # 3. Напишите программу, которая вычислит сумму всех кодов символов
            # строки.

            # Exemple 1

x = input()
s = 0
for item in x:
    s += ord(item)
print(s)

            # Exemple 2

x = input()
s = (ord(item) for item in x)   # генераторное выражение
print(sum(s))

            # 4. Выведите на экран 10 строк со значением числа Pi. В первой строке
            # должно быть 2 знака после запятой, во второй 3 и так далее.

from math import pi

for i in range(2, 10):
    print(f'{pi:.{i}f}')

            # 5. Вводится строка из слов, разделенных пробелами. Найти самое длинное
            # слово и вывести его на экран.

            # Exemple 1

s = input().split()
max_item = s[0]
for item in s:
    if len(item) > len(max_item):
        max_item = item
print(max_item)

            # Exemple 2

s = input().split()
res = max(s, key=len)
print(res)

            # 6. Вовочка сидя на уроке писал подряд одинаковые слова (слово может
            # состоять из одной буквы). Когда Марья Ивановна забрала у него тетрадь,
            # там была одна строка текста. Напишите программу, которая определит
            # самое короткое слово из написанных Вовочкой. Например:
            # aaaaaaa — Вовочка писал слово - «a»
            # ititititit — Вовочка писал слово - «it»
            # catcatcatcat — Вовочка писал слово - «cat»

s = input()
for i in range(len(s) // 2):
    pattern = s[:1]
    if s.count(pattern) * len(pattern) == len(s):
        print(pattern)
        break
else:
    print('Error')

            # 7. Напишите программу для очистки текста от html-тэгов. Больше о htmlтэгах https://html5book.ru/html-tags/
            # Также необходимо учесть пару особенностей:
            # - помимо одинарных тэгов, есть парные тэги, например <div> </div>, т.е.
            # первый тэг открывающий , а второй закрывающий.
            # - тэг внутри себя, может содержать кучу доп. информации.
            # Например <div id="rcnt" style="clear:both;position:relative;zoom:1">

tags_1 = ['p', 'a', 'h1'] # ДОБАВИТЬ ОСТАЛЬНЫЕ ТЕГИ (https://html5book.ru/html-tags/)
html_text = '''
    <h1 sdfgkgkefcpd>dsdfgwfws</h1>
    <p wseefsdfdsfsdgfds <a dfgdsfwfw>sedfrgfregfe</a> </p>
'''
for tag in tags_1:
    while '<' + tag:
        start = html_text.find(f'<tag')
        stop = html_text.find(f'>', start + 1)

        html_text[start, stop +1] = ''

        html_text = html_text.replace(f'</{tag}', '')
