    # 1. Создайте дескриптор, который будет делать поля класса управляемые им
    # доступными только для чтения.

class AreaDescriptor:
    def __get__(self, instance_self,  ):
        p = (instance_self.x + instance_self.y + instance_self.z) / 2
        area = (p * (p - instance_self.x) * (p - instance_self.y) * (p - instance_self.z)) ** 0.5
        return area

    def __set__(self, instance, value):
        raise AttributeError


class Triangle:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    area = AreaDescriptor()

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


x_1 = Triangle(10, 20, 30)
print(x_1.area)
# x_1.volume = 20
print(x_1)

    # 2. Реализуйте функционал, который будет запрещать установку полей класса
    # любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
    # попытаться присвоить, например, строку, то должно быть возбужденно
    # исключение.

class Triangle:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def __setattr__(self, key, value):
        if isinstance(value, int | float):
            self.__dict__[key] = value
        else:
            raise TypeError

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


x = Triangle(1, 2, 3)
print(x)


    # 3. Реализуйте свойство класса, которое обладает следующим
    # функционалом: при установки значения этого свойства в файл с заранее
    # определенным названием должно сохранятся время (когда устанавливали
    # значение свойства) и установленное значение.

import datetime

class Triangle:
    def __init__(self, a, b, c):
        self.x = a
        self.__y = b
        self.__z = c

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        with open('text.txt', 'w') as f:
            res_str = f'{datetime.datetime.now()}, {value}\n'
            f.write(res_str)
            self.__x = value

    def __str__(self):
        return f'{self.x} x {self.__y} x {self.__z}'


x = Triangle(1, 2, 3)
print(x)
print(x.x)

    # 1) Создайте ABC класс с абстрактным методом проверки целого числа на
    # простоту. Т.е., если параметром этого метода является целое число и оно
    # простое, то метод должен вернуть True, а в противном случае False.
    # 2) Создайте класс его наследующий.
    # 3) Создайте класс, который не наследует пользовательский ABC класс, но
    # обладает нужным методом. Зарегистрируйте его в качестве виртуального
    # подкласса.
    # 4) Проверьте работоспособность проекта.

from abc import ABC, abstractmethod


class ABCMyIntNumber(ABC):

    @abstractmethod
    def isprime(self):
        pass


class MyIntNumber(ABCMyIntNumber):

    def __init__(self, number):
        self.number = number

    def isprime(self):
        if not isinstance(self.number, int):
            return False

        for i in range(2, self.number):
            if self.number % i == 0:
                return False

        return True


class MyIntNumber_1:

    def __init__(self, number):
        self.number = number

    def isprime(self):
        if not isinstance(self.number, int):
            return False

        for i in range(2, self.number):
            if self.number % i == 0:
                return False

        return True


x = MyIntNumber(7)
print(x.isprime())

y = MyIntNumber_1(10)
print(y.isprime())

print(isinstance(x, ABCMyIntNumber))
print(isinstance(y, ABCMyIntNumber))

ABCMyIntNumber.register(MyIntNumber_1)

print(isinstance(x, ABCMyIntNumber))
print(isinstance(y, ABCMyIntNumber))