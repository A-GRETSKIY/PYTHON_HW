class PriceError(Exception):

    def __init__(self, price: int | float, message: str):
        super().__init__()
        self.price = price
        self.message = message

    def __str__(self):
        return f'Invalid {self.price}\n {self.message}'


class Product:

    def __init__(self, title, price: int | float):
        if not isinstance(price, int) or not isinstance(price, float) and price <= 0:
            raise PriceError(price, 'Invalid price')
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title} - {self.price}'


pr_1 = Product('apple', 343324345)

print(pr_1)


###


class Person:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name.strip().title()
        self.surname = surname.strip().title()
        self.gender = gender

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.gender}'


class Student(Person):

    def __init__(self, name: str, surname: str, gender: str, age: int):
        super().__init__(name, surname, gender)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'


class GroupLimit(Exception):

    def __init__(self, student, message):
        self.student = student
        self.message = message

    def __str__(self):
        return f'Invalid {self.student}\n {self.message}'


LIMIT = 10


class Group:

    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError()
        if len(self.students) == LIMIT:
            raise GroupLimit(student, 'Quantity of students more then 10')
        if student in self.students:
            raise ValueError('Student already in group')

        self.students.append(student)

    def __str__(self):
        return '\n'.join(map(str, self.students))


st_1 = Student('Ivan', 'Ivanov', 'M', 20)
st_2 = Student('Ivan', 'Ivanov', 'M', 21)
st_3 = Student('Ivan', 'Ivanov', 'M', 22)
st_4 = Student('Ivan', 'Ivanov', 'M', 23)
st_5 = Student('Ivan', 'Ivanov', 'M', 24)
st_6 = Student('Ivan', 'Ivanov', 'M', 25)
st_7 = Student('Ivan', 'Ivanov', 'M', 26)
st_8 = Student('Ivan', 'Ivanov', 'M', 27)
st_9 = Student('Ivan', 'Ivanov', 'M', 28)
st_10 = Student('Ivan', 'Ivanov', 'M', 29)

gr_1 = Group('New')

try:
    gr_1.add_student(st_1)
    gr_1.add_student(st_2)
    gr_1.add_student(st_3)
    gr_1.add_student(st_4)
    gr_1.add_student(st_5)
    gr_1.add_student(st_6)
    gr_1.add_student(st_7)
    gr_1.add_student(st_8)
    gr_1.add_student(st_9)
    gr_1.add_student(st_10)
except Exception as ex:
    print('The group is complete. Create a new group')

print(gr_1)
