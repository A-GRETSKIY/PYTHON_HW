x = int(input('Введите число '))
print(x < 0 and x or 'Больше или равно нулю')

x = int(input('Введите число '))
print(x < 20 and x or 'Больше или равно 20')

x = int(input('Введите число '))
print(x == 0)

# x = int(input('Введите число '))
# print(not bool(x))
#
# x = int(input('Введите число '))
# print(not x)

x = int(input('Введите число: '))
print((x % 2 and 'Число нечетное') or 'Число четное')

# x = int(input('Введите число: '))
# print(not x % 2)
# print(bool(x % 2))

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
print('Максимальное число: ', max(a, b, c))

a, b, c = map(int, input("Введите значение чисел: ").split())
print(max(a, b, c))