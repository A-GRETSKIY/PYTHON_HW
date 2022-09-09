# 1. Реализуйте генераторную функцию, которая будет возвращать по одному
# члену числовой последовательности, закон которой задается с помощью
# пользовательской функции. Кроме этого параметром генераторной функции
# должны быть значение первого члена прогрессии и количество выдаваемых
# членов последовательности (n). Генератор должен остановить свою работу
# или по достижению n — го члена , или при передаче команды на завершение

def arithmetic_progression(a_0, dx, n):
    return a_0 + n * dx


def geom_progression(b_0, q, n):
    return b_0 * q ** (n - 1)


def get_next_item(start: int | float, step: int | float, n: int, func_tool):
    items = (func_tool(start, step, i) for i in range(n))
    while True:
        try:
            yield next(items)
        except:
            break


print(*get_next_item(10, 3, 20, arithmetic_progression))
print(*get_next_item(1, 2, 20, geom_progression))


# 2. Используя функцию замыкания реализуйте такой прием программирования
# как Мемоизация - https://en.wikipedia.org/wiki/Memoization
# Используйте полученный механизм для ускорения функции рекурсивного
# вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
# просто рекурсивным подходом

import timeit


def fibonacci():
    numbers = [0, 1]

    def get_number(n):
        if n < len(numbers):
            return numbers[n]

        curr_item, next_item = numbers[-2], numbers[-1]
        i = len(numbers)

        while i <= n:
            curr_item, next_item = next_item, curr_item + next_item
            numbers.append(next_item)
            i += 1
        return next_item

    return get_number


x = fibonacci()
print(timeit.timeit('x(10)', number=5, setup='from __main__ import x'))


# 3. Напишите функцию, которая применит к списку чисел произвольную
# пользовательскую функцию и вернет суммы элементов полученного списка


def x_2(item):
    return item ** 2


def x_3(item):
    return item ** 3


def x_inc(item):
    return item + 1


def x_dec(item):
    return item - 1


def my_func(seq, func_tool):
    return sum(func_tool(item) for item in seq)


x = (i for i in range(10))
print(my_func(x, x_2))
x = (i for i in range(10))
print(my_func(x, x_3))
x = (i for i in range(10))
print(my_func(x, x_inc))
x = (i for i in range(10))
print(my_func(x, x_dec))