apartment = int(input('Номер квартиры= '))
if 1 <= apartment <= 36:
    print('Подъезд 1')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif 37 <= apartment <= 72:
    print('Подъезд 2')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif 73 <= apartment <= 109:
    print('Подъезд 3')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif 110 <= apartment <= 144:
    print('Подъезд 4')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
else:
    print('Данной квартиры в доме нету!')

# apartment = int(input('Номер квартиры = '))
# if apartment <=144:
#     print('Подъезд: ', (apartment - 1) // 36 + 1)
#     print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
# elif apartment > 144:
#     print('Квартиры нет в данном доме')

x = int(input('Year: '))
if (not x % 4) or (x % 100) and (not x % 400):
    print('Год высокостный')
else:
    print('Год не высокостный')

print('Введите длинну сторон треугольника')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Треугольник существует')
else:
    print('Треугольник НЕ существует')