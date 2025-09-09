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
        self.grades = {}  # ключи — названия курсов, значения — списки оценок

    def _average_grade(self):
        """Вспомогательный метод: вычисляет среднюю оценку по всем курсам."""
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self):
        avg = self._average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg:.1f}"

    # Методы сравнения
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
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Выставляет студенту оценку за домашнюю работу по курсу."""
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
        self.grades = {}  # оценки от Reviewer'ов

    def rate_lecture(self, lecturer, course, grade):
        """Выставляет лектору оценку за лекцию."""
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
        """Вспомогательный метод: вычисляет среднюю оценку за домашние задания."""
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

    # Методы сравнения
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