    # 1. Создайте декоратор, который будет подсчитывать, сколько раз была
    # вызвана декорируемая функция

            ### VAR.1 - РЕАЛИЗОВАНО НА ЭФФЕКТЕ ЗАМЫКАНИЯ

def decorator(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs), count

    return inner


@decorator
def greetings(name):
    return f'Hello, {name}'


print(greetings('Oleh'))
print(greetings('Ivan'))

            ### VAR.2 - РЕАЛИЗОВАНО НА ООП

def decorator(func):

    def inner(*args, **kwargs):
        inner.count += 1
        return func(*args, **kwargs)

    inner.count = 0

    return inner

@decorator
def greetings(name):
    return f'Hello, {name}'


print(greetings('Oleh'), greetings.count)
print(greetings('Ivan'), greetings.count)

    # 2. Создайте декоратор, который зарегистрирует декорируемую функцию в
    # списке функций, для обработки последовательности

            ### VAR.1

func_list = []

def decorator(func):
    func_list.append(func)
    return func

@decorator
def x_2(item):
    return item ** 2

@decorator
def x_3(item):
    return item ** 3


x = [i for i in range(10)]

for func in func_list:
    print(list(map(func, x)))

            ### VAR.2

def decorator(func):
    decorator.lst.append(func)
    return func

decorator.lst = []

@decorator
def x_2(item):
    return item ** 2

@decorator
def x_3(item):
    return item ** 3


x = [i for i in range(10)]

for func in decorator.lst:
    print(list(map(func, x)))

    # 3. Предположим, в классе определен метод __str__, который возвращает
    # строку на основании класса. Создайте такой декоратор для этого метода,
    # чтобы полученная строка сохранялась в текстовый файл, имя которого
    # совпадает с именем класса, метод которого вы декорировали


def decorator(func):
    def inner(*args, **kwargs):
        names = func.__qualname__.split('.')[:-1]
        file = '.'.join(names) + '.txt'
        res = func(*args, **kwargs)
        with open(file, 'w') as f:
            f.write(res)
        return res
    return inner


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @decorator
    def __str__(self):
        return f'{self.name}, {self.name}'


x = Person('Ivan', 20)
print(x)

    # 4. Создайте декоратор с параметрами для проведения хронометража работы
    # той или иной функции. Параметрами должны выступать то, сколько раз нужно
    # запустить декорируемую функцию и в какой файл сохранить результаты
    # хронометража. Цель - провести хронометраж декорируемой функции.

import time

def decorator(file_name, number):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()

            for i in range(number):
                res = func(*args, **kwargs)

            stop = time.time()
            with open(file_name, 'w') as f:
                f.write(f'{start} : {stop} : {stop-start}')
            return res
        return inner
    return wrapper

@decorator('test.txt', 5)
def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

print(fibonacci(30))

    # 1. Создайте декоратор, который зарегистрирует декорируемый класс в
    # списке классов

list_classes = []

def add_class(cls):
    list_classes.append(cls)
    return cls

@add_class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age }'

@add_class
class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


x = list_classes[0]('Ivan', 20)
y = list_classes[1](10, 20, 30)

print(x)
print(y)

    # 2. Создайте декоратор класса с параметром. Параметром должна быть
    # строка, которая должна дописываться (слева) к результату работы метода
    # __str__.

class DecoratorClass:

    def __init__(self, cls):
        self.param = 'Hello'
        self.cls = cls

    def __call__(self, *args, **kwargs):
        self.new_instance = self.cls(*args, **kwargs)
        return self

    def __str__(self):
        return f'{self.param} {self.new_instance}'

@DecoratorClass
class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


x = Box(10, 20, 30)
print(x)

# 3. Для класса Box напишите статический метод, который будет подсчитывать
# суммарный объем двух ящиков, которые будут его параметрами

class Box:

    count = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Box.count += 1

    @classmethod
    def boxes_number(cls):
        return cls.count

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def summa_volumes(a, b):
        if isinstance(a, Box) and isinstance(b, Box):
            return a.volume() + b.volume()
        return None


x = Box(1, 2, 3)
y = Box(10, 20, 30)

print(Box.boxes_number())