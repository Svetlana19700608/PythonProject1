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

    def _average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self):
        avg = self._average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg:.1f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() == other._average_grade()


class Reviewer(Mentor):
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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


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

    def _average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self):
        avg = self._average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет"
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg:.1f}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() == other._average_grade()


# 📌 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

def average_grade_students(students, course):
    """Считает среднюю оценку за домашние задания по всем студентам в рамках курса."""
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0.0


def average_grade_lecturers(lecturers, course):
    """Считает среднюю оценку за лекции всех лекторов в рамках курса."""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0.0


# 🎯 СОЗДАНИЕ ЭКЗЕМПЛЯРОВ

# Студенты
student1 = Student('Анна', 'Иванова', 'женский')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Иван', 'Петров', 'мужской')
student2.courses_in_progress += ['Python', 'C++']
student2.finished_courses += ['Алгоритмы']

# Лекторы
lecturer1 = Lecturer('Алексей', 'Сидоров')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Мария', 'Козлова')
lecturer2.courses_attached += ['Python', 'C++']

# Эксперты
reviewer1 = Reviewer('Олег', 'Смирнов')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Елена', 'Васильева')
reviewer2.courses_attached += ['Python', 'C++']


# 🧪 ВЫЗОВ ВСЕХ МЕТОДОВ

# Эксперты выставляют оценки студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 10)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student2, 'Python', 9)

# Студенты выставляют оценки лекторам
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Git', 9)
student1.rate_lecture(lecturer2, 'Python', 8)  # Ошибка — лектор2 не ведёт Git у student1, но Python — да

student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'C++', 8)
student2.rate_lecture(lecturer1, 'Python', 7)  # OK — оба на Python

# Попытка ошибочного выставления
print("Попытка оценить не лектора:")
print(student1.rate_lecture(reviewer1, 'Python', 5))  # => Ошибка

print("\n" + "="*50 + "\n")

# Вывод информации через __str__
print("Reviewer 1:")
print(reviewer1)
print("\nReviewer 2:")
print(reviewer2)

print("\nLecturer 1:")
print(lecturer1)
print("\nLecturer 2:")
print(lecturer2)

print("\nStudent 1:")
print(student1)
print("\nStudent 2:")
print(student2)

print("\n" + "="*50 + "\n")

# Сравнение студентов и лекторов
print("Сравнение студентов:")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")

print("\nСравнение лекторов:")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

print("\n" + "="*50 + "\n")

# Подсчёт средних оценок по курсам
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка студентов по курсу 'Python': {average_grade_students(students_list, 'Python'):.1f}")
print(f"Средняя оценка студентов по курсу 'Git': {average_grade_students(students_list, 'Git'):.1f}")
print(f"Средняя оценка лекторов по курсу 'Python': {average_grade_lecturers(lecturers_list, 'Python'):.1f}")
print(f"Средняя оценка лекторов по курсу 'C++': {average_grade_lecturers(lecturers_list, 'C++'):.1f}")