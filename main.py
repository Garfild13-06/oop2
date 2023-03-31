class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.averageGrade()}\n" \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершённые курсы: {', '.join(self.finished_courses)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student!")
            return
        else:
            if self.averageGrade() < other.averageGrade():
                return f"У студента {self.name} {self.surname} средний бал меньше ({self.averageGrade()}), чем у {other.name} {other.surname} ({other.averageGrade()})"
            elif self.averageGrade() > other.averageGrade():
                return f"У студента {self.name} {self.surname} средний бал больше ({self.averageGrade()}), чем у {other.name} {other.surname} ({other.averageGrade()})"

    def averageGrade(self):
        summ = 0
        for grade in self.grades.values():
            summ += grade[0]
        res = summ / len(self.grades)
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.averageGrade()}"
        return res

    def averageGrade(self):
        summ = 0
        if len(self.grades) == 0:
            return
        else:
            for grade in self.grades.values():
                summ += grade[0]
            res = summ / len(self.grades)
            return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        else:
            if self.averageGrade() < other.averageGrade():
                return f"У лектора {self.name} {self.surname} средний бал меньше ({self.averageGrade()}), чем у {other.name} {other.surname} ({other.averageGrade()})"
            elif self.averageGrade() > other.averageGrade():
                return f"У лектора {self.name} {self.surname} средний бал больше ({self.averageGrade()}), чем у {other.name} {other.surname} ({other.averageGrade()})"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def students_grades_avg(students_list, course):
    summ = 0
    count = 0
    for student in students_list:
        try:
            count += len(student.grades[course])
            for grade in student.grades[course]:
                summ += grade
        except:
            pass
    res = f"Средняя оценка для студентов по предмету {course}: {summ / count}"
    return res


def lectures_grades_avg(lectures_list, course):
    summ = 0
    count = 0
    for lecture in lectures_list:
        try:
            count += len(lecture.grades[course])
            for grade in lecture.grades[course]:
                summ += grade
        except:
            pass
    res = f"Средняя оценка для лекторов по предмету {course}: {summ / count}"
    return res


# Создаём Студентов
student_1 = Student('Harry', 'Potter', 'male')
student_1.courses_in_progress += ['Python', 'JS']
student_2 = Student('Hermione', 'Granger', 'female')
student_2.courses_in_progress += ['Python', 'HTML']
# Создаём Лекторов
lecturer_1 = Lecturer('Albus', 'Dambldor')
lecturer_1.courses_attached += ['Python', 'Java', 'Ruby']
lecturer_2 = Lecturer('Sirius', 'Black')
lecturer_2.courses_attached += ['Python', 'Ruby', 'HTML', 'JS']
# Создаём проверяющих
reviewer_1 = Reviewer('Andrey', 'Palmer')
reviewer_2 = Reviewer('Jocn', 'Uick')
# Студенты ставят оценки Лекторам
student_1.rate_lw(lecturer_1, 'Python', 7)
student_1.rate_lw(lecturer_2, 'Ruby', 10)
student_2.rate_lw(lecturer_1, 'Java', 7)
student_2.rate_lw(lecturer_2, 'HTML', 10)
student_2.rate_lw(lecturer_2, 'Python', 8)
# Проверяющие ставят оценки Студентам
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Ruby', 7)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_1, 'JS', 8)
reviewer_2.rate_hw(student_2, 'HTML', 6)
# Сравниваем Студентов
print("---Сравниваем студентов---")
print(student_1 < student_2)
# Сравниваем Лекторов
print("\n---Сравниваем лекторов---")
print(lecturer_1 < lecturer_2)
# Выводим Студентов
print("\n---Вывод студентов---")
print(student_1)
print(student_2)
# Выводим Лекторов
print("\n---Вывод лекторов---")
print(lecturer_1)
print(lecturer_2)
# Выводим Проверяющих
print("\n---Вывод проверяющих---")
print(reviewer_1)
print(reviewer_2)
# Выводим средних оценок по студентам и лекторам
print("\n---Вывод средних оценок по студентам и лекторам---")
print(students_grades_avg([student_1, student_2], "Python"))
print(lectures_grades_avg([lecturer_1, lecturer_2], "Python"))
