a = int(str('123'))
print(a)

a = float(int(123))
print(a)

a = int(float(123.45))
print(a)

d = int(input('Введите номер карты: '))
print('Последние 4 цифры: ', d % 10000)

x = int(input('Введите 3-х значное число: '))
print(x // 100 + x // 10 % 10 + x % 10)

print('Введите длинну сторон треугольника')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('Площадь треугольника =', s)

a = input('Введите число: ')
a = sum(map(int, str(a)))
print('Сумма цифр: ', a)

a = input('Введите число: ')
print('Колличество цифр: ', len(a))

a = input('Введите число: ')
print('Цифры в обратном порядке: ', a[::-1])