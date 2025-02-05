class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        # Проверяем, является ли лектора экземпляром класса Lecturer
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)  # Добавляем оценку к существующим
            else:
                lecturer.grades[course] = [grade]  # Создаем новый список оценок
        else:
            return 'Ошибка: Невозможно выставить оценку.'

    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            averg = sum(all_grades) / len(all_grades)
        else:
            averg = 0
        return averg

    def __ge__(self, lector):
        if isinstance(lector, Lecturer):
            return self.avr() >= new_lector.avr()
        else:
            return NotImplemented

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.avr():.2f}\n'
                f'Курсы в процессе изучения:{",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)} ')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для оценок, выставленных студентами

    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            averg = sum(all_grades) / len(all_grades)
        else:
            averg = 0
        return averg

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avr():.2f} '


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка: Невозможно выставить оценку.'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student.finished_courses.append('Введение в программирование')
best_student1 = Student('Bill', 'Gate', 'male')
best_student1.courses_in_progress.append('C#')
best_student1.finished_courses.append('C++')
best_student.courses_in_progress.append('C#')

new_lector = Lecturer('Nik', 'Chern')
new_lector.courses_attached.append('Python')
new_lector1 = Lecturer('Max', 'Payne')
new_lector1.courses_attached.append('C#')

new_rew = Reviewer('Artem', 'Dobovs')
new_rew.courses_attached.append('Python')
new_rew1 = Reviewer('Jan', 'Clode')
new_rew1.courses_attached.append('C#')


best_student1.rate_hw(new_lector1, 'C#', 6)
best_student.rate_hw(new_lector, 'Python', 8)
best_student.rate_hw(new_lector1, 'C#', 10)


new_rew1.rate_hw(best_student1, 'C#', 10)
new_rew.rate_hw(best_student, 'Python', 7)
new_rew1.rate_hw(best_student,'C#',2)

if best_student.avr() >= new_lector.avr():
    print(best_student.name, 'bigger avr than', new_lector.name)
else:
    print(new_lector.name, 'bigger avr than', best_student.name)
print()
print(new_rew)
print()
print(new_lector)
print()
print(best_student)
print()
print(new_rew1)
print()
print(new_lector1)
print()
print(best_student1)
