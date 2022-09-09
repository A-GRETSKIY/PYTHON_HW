        # 1. Напишите регулярное выражение, которое будет находить в тексте фрагменты, состоящие из одной буквы R,
        # за которой следует одна или более букв b, за которой одна r. Учитывать верхний и нижний регистр.

import re

pattern = r'(Rb+r)'
text = 'rbbbbbrRbbrRbr'

res = re.findall(pattern, text)
print(res)

        # 2. Напишите функцию, выполняющую валидацию номера банковской карты (9999-9999-9999-9999).

        # Var. 1

pattern = r'^(\d{4}-\d{4}-\d{4}-\d{4})$'
text = '1234-1234-1234-1234'

res = re.search(pattern, text)
print(res)

        # Var. 2

def validate_credit_cards(credit_cards):
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    for cc in credit_cards:
        if all(re.match(f, cc) for f in filters):
            print(f"{cc} is Valid")
        else:
            print(f"{cc} is Invalid")


credit_cards = ['2536258796157802','4253625879615786',
          '4424424424442444', '5122-2368-7954-3214',
          '4424444424442444']
validate_credit_cards(credit_cards)

        # 3. Напишите функцию, принимающую строковые данные и выполняющую проверку на их соответствие мейлу.
        # Требования:
        # -цифры (0-9).
        # -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
        # -в теле мейла допустимы только символы “_” и “-”. Но они не могут быть первым символом мейла.
        # -символ “-” не может повторяться.

        # Var. 1

pattern = r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'
# pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
text = 'ag_rek@gmail.com'

res = re.search(pattern, text)
print(res)

        # Var. 2

regex = re.compile(r'([a-zA-Z0-9]+[.-_])*[a-zA-Z0-9]+@[a-zA-Z0-9-]+(\.[a-z|A-Z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")

isValid("name.surname@gmail.com")
isValid("anonymous123@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("...@domain.us")

        # 4. Напишите функцию, проверяющую правильность логина. Правильный логин – строка от 2 до 10 символов,
        # содержащая только буквы и цифры.

        # Var. 1

pattern = r'^\w{2,10}$'
text = 'qwerty1234'

res = re.findall(pattern, text)
print(res)

        # Var. 2

pattern = r'^([a-zA-Z0-9]){2,10}$'
text = 'qwerty1234'

res = re.findall(pattern, text)
print(res)