            # 1. Выведите на экран все числа в диапазоне от 1 до 100 кратные 7

            # Exemple 1

dx = 7
i = 7
while i <= 100:
    print(i)
    i += dx

            # Exemple 2

dx = 7
i = 0
while i <= 100:
    i += dx
    print(i)  # ВЫВОДИТ ЕЩЕ И 105

            # Exemple 3

for a in range(7, 100, 7):
    print(a)

            # Exemple 4

for a in range(1, 100):
    if not a % 7:
        print(a)

            # 2. Вычислить с помощью цикла факториал числа n введенного с
            # клавиатуры (4<n<16). Факториал числа - это произведение всех чисел от
            # этого числа до 1. Например, 5!=5*4*3*2*1=120

            # Exemple 1

n = int(input('Введите число: '))
f = 1
for i in range(2, n + 1):
    f *= i
print(f)

            # Exemple 2

n = int(input('Введите число: '))
f = n
for i in range(2, n):
    f *= i
print(f)

            # Exemple 3

import math

n = int(input('Введите число: '))
print(math.factorial(n))

            # 3. Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
            # = 5, 2 x 5 = 10, а не просто 5, 10 и т. д.

for n in range(1, 11):
    print(15 * '*', n, 15 * '*')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')

            # 4. Выведите на экран прямоугольник из *. Причем, высота и ширина
            # прямоугольника вводятся с клавиатуры. Например, ниже представлен
            # прямоугольник с высотой 4 и шириной 5.
            # *****
            # *   *
            # *   *
            # *****

            # Exemple 1

n = int(input("n "))
m = int(input("m "))
part_1 = f"{'*' * n}\n"
part_2 = (m - 2) * f"*{' ' * (n - 2)}*\n"
res = part_1 + part_2 + part_1
print(res)

            # Exemple 2

n = int(input("n "))
m = int(input("m "))
x = f"{'*' * n}\n" + (m - 2) * f"*{' ' * (n - 2)}*\n" + f"{'*' * n}\n"
print(x)

            # Exemple 3

n = int(input("n "))
m = int(input("m "))
mid = (m - 2) * f"*{' ' * (n - 2)}*\n"
res = f"{'*' * n}\n{mid}{'*' * n}\n"
print(res)

            # 5. С помощью циклов вывести на экран все простые числа от 1 до 100.
            # Простое число — число, которое делится нацело только на единицу или само
            # на себя. Первые простые числа это — 2,3,5,7…

for n in range(1, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

            # 6. Выведите на экран «песочные часы», максимальная ширина которых
            # считывается с клавиатуры (число нечетное). В примере ширина равна 5.
            # *****
            #  ***
            #   *
            #  ***

n = int(input('n = '))
space = 0
for i in range(n, 0, -2):  # i - это звездочки
    print(f"{' ' * space}{'*' * i}")
    space += 1
space -= 2
for i in range(3, n + 1, 2):
    print(f"{' ' * space}{'*' * i}")
    space -= 1
