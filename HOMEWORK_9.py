# 1. Напишите функцию, которая вернет максимальное число из списка
# чисел.

# 1

def max_item(x):
    return max(x)


print(max_item([1, 2, 3, 4, 5]))


# 2

def max_item(*x):  ### args (*) говорит о том, что в 'x' может быть больше 1 обьекта. Тип данных будет кортеж
    return max(x)


print(max_item(*[1, 2, 3, 4, 5]))  ### (*) перед списком [] - раскаковка


# 3

def max_item(**kwargs):  ### kwargs (**)
    return kwargs


print(max_item(a=1, b=2, c=3))  ### будет словарь, МАКС.ЧИСЛО НЕ ВЫВОДИТ !!!!!


# 4
### *args, ** kwargs - добавлять в функцию !!!!!!!!! на случай ее расширения

def max_item(*args, **kwargs):  ### позиционные элем. попадут в кортеж, ост. в словарь
    print(args)
    print(kwargs)
    return max(args + tuple(kwargs.values()))


print(max_item(1, 2, 3, 4, a=1, b=2, c=3))


# 2. Реализуйте функцию, параметрами которой являются - два числа и
# строка. Возвращает она конкатенацию строки с суммой чисел.

def summa(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, str):
        return None
    return f'{a + b}{c}'


print(summa(5, 10, 'www'))


# 3. Реализуйте функцию рисующую на экране прямоугольник из звездочек
# «*». Ее параметрами будут целые числа, которые описывают длину и
# ширину такого прямоугольника.

def rectangle(n, m):
    if not isinstance(n, int) or not isinstance(m, int):
        return None

    return '*' * m + '\n' + (n - 2) * ('*' + ' ' * (m - 2) + '*' + '\n') + '*' * m


print(rectangle(5, 10))


# 4. Напишите функцию, которая реализует линейный поиск элемента в
# списке целых чисел. Если такой элемент в списке есть, то верните его
# индекс, если нет, то верните число «-1».

def search(x, seq):
    for i, item in enumerate(seq):
        if item == x:
            return 1
    return -1


### print(search(3, [10, 2, 4, 5, 6])) - вариант проверки

# 5. Напишите функцию, которая вернет количество слов в строке текста.


def words(text):
    return len(text.split())

    # return text.count(' ') + 1

    # 6. Существуют такие последовательности чисел:
    # 0,2,4,6,8,10,12   (+2)
    # 1,4,7,10,13       (+3)
    # 1,2,4,8,16,32     (*2)
    # 1,3,9,27          (*3)
    # 1,4,9,16,25       (**2)
    # 1,8,27,64,125     (**3)
    # Реализуйте программу, которая выведет следующий член этой
    # последовательности (либо подобной им) на экран. Последовательность
    # пользователь вводит с клавиатуры в виде строки. Например, пользователь
    # вводит строку 0,5,10,15,20,25 и ответом программы должно быть число 30.


# 0,2,4,6,8,10,12 and # 1,4,7,10,13 (арифм.посл., +2 и +3)
def is_ariphmetic(x):
    d = x[1] - x[0]
    for i in range(len(x) - 1):
        if x[i + 1] - x[i] != d:
            return False
    return True


# 1,2,4,8,16,32 - (a - показатель степени)
def is_pow_a(x, a):
    for i, item in enumerate(x):
        if item != a ** i:
            return False
    return True


# 1,8,27,64,125 - (b - показатель степени)
def is_pow_b(x, b):
    for i, item in enumerate(x):
        if item != (i + 1) ** b:
            return False
    return True


def seq_detect(x):
    if is_ariphmetic(x):
        pass
    elif is_pow_a(x, 2):
        pass
    elif is_pow_a(x, 3):
        pass
    elif is_pow_b(x, 3):
        pass
    else:
        return None

    # 7. Число-палиндром с обеих сторон (справа налево и слева направо)
    # читается одинаково. Самое большое число-палиндром, полученное
    # умножением двух двузначных чисел: 9009 = 91 × 99. Найдите самый
    # большой палиндром, полученный умножением двух трехзначных чисел.
    # Выведите значение этого палиндрома и то, произведением каких чисел он
    # является.


def polindrom():
    max_polindrom = 0
    a, b = -1, -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            tmp = i * j
            tmp_str = str(tmp)
            if tmp_str == tmp_str[::-1]:
                max_polindrom, a, b = (tmp, i, j) if tmp > max_polindrom else (max_polindrom, a, b)
    return max_polindrom, a, b


print(polindrom())