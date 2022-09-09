            # 1.Напишите программу, которая считает две строки текста с клавиатуры и
            # выведет на экран буквы, которые есть одновременно и в первой, и во
            # второй строке. Например, для строк «Hello» и «World» на экране должны
            # быть буквы «l» и «o».

text_1 = set(input('text_1 = '))
text_2 = set(input('text_2 = '))
print(text_1 & text_2)

            # 2.Напишите программу, которая сгенерирует два списка. Один с числами
            # кратными 3, другой с числами кратными 5. С помощью множеств
            # создайте список с числами, которые есть в обоих множествах.

            # Exemple 1

a = []
for i in range(3, 100, 3):
    a.append(i)
b = []
for j in range(5, 100, 5):
    b.append(j)
res = set(a) & set(b)
print(res)

            # Exemple 2

### ЧЕРЕЗ LIST COMPREHENSIONS
x = [i for i in range(100) if not i % 3]
y = [i for i in range(100) if not i % 3]
print(set(x) & set(y))

x = [i for i in range(100) if not i % 3]
y = [i for i in range(100) if not i % 5]
print(sorted(set(x) & set(y))) # СОРТИРУЕТ, НО РЕЗУЛЬТАТ В ВИДЕ СКИСКА, А НЕ МНОЖЕСТВА
