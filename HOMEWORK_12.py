class Person:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name.strip().title()  # STRIP УБИРАЕТ НЕПЕЧАТАЕМЫЕ СИМВОЛЫ СЛАВА И СПРАВА
        self.surname = surname.strip().title()  # TITLE , ЧТО БЫ ИМЯ И ФАМ. БЫЛИ С БОЛЬШОЙ БУКВЫ
        self.gender = gender

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.gender}'


class Student(Person):

    def __init__(self, name: str, surname: str, gender: str, age: int):
        super().__init__(name, surname, gender)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'  # ЧЕРЕЗ ФУНК. SUPER ВЫЗЫВАЕТСЯ МЕТОД STR БАЗОВОГО КЛАССА


LIMIT = 10


class Group:

    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if student not in self.students and len(self.students) < LIMIT:
            self.students.append(student)

    def del_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)

    def search_by_surname(self, value):
        res = [stud for stud in self.students if stud.surname == value]
        return res or None  # return res if res else None # ЕСЛИ В СПИСКЕ ЕСТЬ ЭЛЕМ.-ВЕРНУТЬ ЭТОТ СПИСОК, ИНАЧЕ-NONE

    def search_by_chr(self, value):  # НАЧИНАЕТСЯ ЛИ ФАМИЛИЯ НА КАКОЙ-ТО СИМВОЛ??? МЕТОД - startswith
        res = [stud for stud in self.students if stud.surname.startswith(value) or stud.name.startswith(value)]
        return res if res else None  # return res or None

    def __str__(self):
        return '\n'.join(map(str, self.students))


students = [Student('Ivan', f'Ivanov{i}', 'M', 20 + i) for i in range(20)]
gr_1 = Group('New')
for item in students:
    gr_1.add_student(item)

print(gr_1)  # выводит всех студентов

gr_1.del_student(students[0])  # удаляет студента по индексу

print(gr_1.search_by_chr('Ivanov2'))  # выводит по символам, но как объекты

for item in gr_1.search_by_chr('Ivanov2'):
    print(item)  # выводит по символам, но в стандартный поток вывода
