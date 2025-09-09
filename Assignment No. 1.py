class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # список курсов, к которым прикреплён ментор

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.grades = {}

    def __str__(self):
        return f"Лектор\n{super().__str__()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def __str__(self):
        return f"Эксперт\n{super().__str__()}"
