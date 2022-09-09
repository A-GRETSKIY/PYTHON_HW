# 1) Реализуйте генераторную функцию, которая будет возвращать по
# одному члену геометрической прогрессии с указанным множителем.
# Генератор должен остановить свою работу или по достижению указанной
# границы, или при передаче команды на завершение.


def geom(q, stop):
    index = 1

    # 1*q, 2*q, 3*q
    while index * q < stop:
        yield index * q
        index += 1

x = geom(2, 200)
for item in x:
    print(item)


# 2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
# знаете, что это - генератор.


def my_range(*args):
    # my_range(10)
    # my_range(10, 100)
    # my_range(10, 100, 3)

    start, stop, step = 0, None, 1
    for item in args:
        if not isinstance(item, int):
            raise TypeError('Error 1')

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError('Error 2')

    while start < stop:
        yield start
        start += step


for i in my_range(10):
    print(i)


# 3) Напишите функцию-генератор, которая будет возвращать простые числа.
# Верхняя граница этого диапазона должна быть задана параметром этой
# функции.


def prime_numbers(stop):
    for n in range(1, stop):
        for i in range(2, n):
            if not n % i:
                break
        else:
            yield n


for i in prime_numbers(100):
    print(i)


# 4) Напишите выражение-генератор для заполнения списка. Список должен
# быть заполнен кубами чисел от 2 и до указанной вами величины.


n = int(input('n = '))
x = (i ** 2 for i in range(1, n))

print(x)
# print(*x)

y = list(x)
print(y)
