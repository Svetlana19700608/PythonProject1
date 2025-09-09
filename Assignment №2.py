class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        return f"Лектор\n{super().__str__()}\nОценки: {self.grades}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Эксперт\n{super().__str__()}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):

        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        if not (0 <= grade <= 10):
            return 'Ошибка'

        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return None

    def __str__(self):
        return f"Студент\nИмя: {self.name}\nФамилия: {self.surname}\nКурсы в процессе: {self.courses_in_progress}"