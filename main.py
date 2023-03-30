class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
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
        return self.averageGrade() < other.averageGrade()

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
        for grade in self.grades.values():
            summ += grade[0]
        res = summ / len(self.grades)
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        return self.averageGrade() < other.averageGrade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JS']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

new_reviewer = Reviewer('Seth', 'Dougan')
new_reviewer.courses_attached += ['Python']
new_reviewer.rate_hw(best_student, 'Python', 10)

new_lecturer = Lecturer('Alex', 'Griffin')
new_lecturer.courses_attached += ['Python']
new_lecturer.courses_attached += ['JS']

best_student.rate_hw(new_lecturer, 'Python', 5)
best_student.rate_hw(new_lecturer, 'JS', 7)

print(best_student)
print(new_lecturer)
print(new_reviewer)
