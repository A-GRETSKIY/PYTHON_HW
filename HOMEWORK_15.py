class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __add__(self, other):
        return Rectangle(1, self.square() + other.square())

    def __mul__(self, n):
        return Rectangle(1, self.square() * n)

    def __str__(self):
        return f'{self.width} x {self.height}'


rec_1 = Rectangle(2, 3)
rec_2 = Rectangle(2, 4)

print(rec_1 > rec_2)
print(rec_1 + rec_2)
print(rec_2 * 2)

                    ###
                    
import math


class Rational:

    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError("A must be integer")
        if not isinstance(b, int):
            raise TypeError("B must be integer")
        if b == 0:
            raise ZeroDivisionError("Number can't be zero")
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.a + other * self.b, self.b)

        if isinstance(other, Rational):
            return Rational(self.a * other.b + other.a * self.b, self.b * other.b)

        raise TypeError('Unsupported data type')

    def __sub__(self, other):
        if isinstance(other, int):
            return Rational(self.a - other * self.b, self.b)

        if isinstance(other, Rational):
            return Rational(self.a * other.b - other.a * self.b, self.b * other.b)

        raise TypeError('Unsupported data type')

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.a * other, self.b)

        if isinstance(other, Rational):
            return Rational(self.a * other.a, self.b * other.b)

        raise TypeError('Unsupported data type')

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.a, other * self.b)

        if isinstance(other, Rational):
            return Rational(self.a * other.b, self.b * other.a)

        raise TypeError('Unsupported data type')

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __ge__(self, other):
        return self.a / self.b >= other.a / other.b

    def __le__(self, other):
        return self.a / self.b <= other.a / other.b

    def __str__(self):
        if self.a / self.b > 1:
            return f'{self.a // self.b} ({self.a - self.a // self.b * self.b} / {self.b})'
        tmp = math.gcd(self.a, self.b)
        return f'{self.a // tmp} / {self.b // tmp}'


num_1 = Rational(2, 3)
num_2 = Rational(1, 2)

print(num_1 / num_2)

                    ###
                    
class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        elif type(numerator) is not int or type(denominator) is not int:
            raise TypeError("numerator and denominator must be integers")

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        common_factor = gcd(numerator, denominator)
        self.numer = numerator // common_factor
        self.denom = denominator // common_factor

    def __str__(self):
        if self.denom != 1:
            return f"{self.numer}/{self.denom}"
        else:
            return str(self.numer)

    def __float__(self):
        return self.numer / self.denom

    def __eq__(self, other):
        if type(other) is Fraction:
            return self.numer == other.numer and self.denom == other.denom
        else:
            return float(self) == other

    def __add__(self, other):
        return self.numer * other.numer + self.denom * other.denom, self.denom * other.denom

    def __sub__(self, other):
        return self.numer * other.numer - self.denom * other.denom, self.denom * other.denom

    def __mul__(self, other):
        return self.numer * other.numer, self.denom * other.denom

    def __truediv__(self, other):
        if self.denom * other.numer == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Fraction(self.numer * other.denom, self.denom * other.numer)


num_1 = Fraction(2, 3)
num_2 = Fraction(1, 2)

print(num_1 / num_2)
