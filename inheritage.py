class Student:                                      # класс студентов
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        summ = 0                                               # средний балл
        n = 0
        for i in self.grades.values():
            for k in i:
               summ += k
               n += 1
        average = summ/n
        progress = ", ".join(self.courses_in_progress)          # изучаемые курсы
        finished = ", ".join(self.finished_courses)             # завершённые курсы
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {average} \n" \
               f"Курсы в процессе изучения: {progress} \n" \
               f"Завершённык курсы: {finished} \n"

    def course_controle(self):
        summ = 0  # средний балл
        n = 0
        for i in self.grades.values():
            for k in i:
                summ += k
                n += 1
        average = summ / n  # средняя оценка за лекции
        return (average)

                                                     # студенты оценивают лекторов

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:                                        # класс преподов
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):                              # подкласс лекторов
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        summ = 0                                  # средний балл
        n = 0
        for i in self.grades.values():
            for k in i:
                summ += k
                n += 1
        average = summ / n                          # средняя оценка за лекции
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {average} \n"

    def mentor_controle(self):
        summ = 0                                   # средний балл по лекциям
        n = 0
        for i in self.grades.values():
            for k in i:
                summ += k
                n += 1
        average = summ / n  # средняя оценка за лекции
        return (average)
                                                       # преподы оценивают студентов

class Reviewer(Mentor):                                 # подкласс ревьюеров

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n"



student_list = []
best_student = Student('Ruoy', 'Eman', 'male')      # добавляем данные о студенте
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java Script']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Telebot course']
best_student.finished_courses += ['Starting new career']
student_list.append(best_student)

ever_better_student = Student('Troy', 'Sylvan', 'female')
ever_better_student.courses_in_progress += ['Python']
ever_better_student.courses_in_progress += ['Java Script']
ever_better_student.courses_in_progress += ['C++']
ever_better_student.finished_courses += ['Telebot course']
ever_better_student.finished_courses += ['Hackatron']
student_list.append(ever_better_student)


cool_mentor = Reviewer('Severus', 'Sniper')                   # добавляем данные о ревьюерах
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java Script']
de_mentor = Reviewer('Zoltan', 'Ferguson')
de_mentor.courses_attached += ['Java Script']
de_mentor.courses_attached += ['C++']


cool_mentor.rate_hw(best_student, 'Python', 10)           # препод ставит оценки
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Java Script', 7)
cool_mentor.rate_hw(best_student, 'Java Script', 8)
cool_mentor.rate_hw(best_student, 'Java Script', 6)
cool_mentor.rate_hw(ever_better_student, 'Python', 6)
cool_mentor.rate_hw(ever_better_student, 'Python', 10)
cool_mentor.rate_hw(ever_better_student, 'Python', 10)
cool_mentor.rate_hw(ever_better_student, 'Java Script', 9)
cool_mentor.rate_hw(ever_better_student, 'Java Script', 9)
cool_mentor.rate_hw(ever_better_student, 'Java Script', 8)

de_mentor.rate_hw(best_student, 'Java Script', 8)
de_mentor.rate_hw(best_student, 'Java Script', 9)
de_mentor.rate_hw(best_student, 'Java Script', 7)
de_mentor.rate_hw(best_student, 'C++', 7)
de_mentor.rate_hw(best_student, 'C++', 3)
de_mentor.rate_hw(best_student, 'C++', 9)
de_mentor.rate_hw(ever_better_student, 'C++', 5)
de_mentor.rate_hw(ever_better_student, 'C++', 9)
de_mentor.rate_hw(ever_better_student, 'C++', 8)


lecturer_list = []
best_lecturer = Lecturer('Alfred', 'Lasarus')               # назначаем лекторов
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['C++']
best_lecturer.courses_attached += ['Java Script']
lecturer_list.append(best_lecturer)

true_lecturer = Lecturer('David', 'Tennant')
true_lecturer.courses_attached += ['Python']
true_lecturer.courses_attached += ['C++']
true_lecturer.courses_attached += ['Java Script']
lecturer_list.append(true_lecturer)


best_student.rate(best_lecturer, 'Python', 10)                # студенты оценивают лекторов
best_student.rate(best_lecturer, 'Python', 8)
best_student.rate(best_lecturer, 'Python', 9)
best_student.rate(best_lecturer, 'Java Script', 5)
best_student.rate(best_lecturer, 'Java Script', 9)
best_student.rate(best_lecturer, 'Java Script', 9)
best_student.rate(best_lecturer, 'C++', 9)
best_student.rate(best_lecturer, 'C++', 2)
best_student.rate(best_lecturer, 'C++', 7)
best_student.rate(true_lecturer, 'Python', 9)
best_student.rate(true_lecturer, 'Python', 8)
best_student.rate(true_lecturer, 'Python', 9)
best_student.rate(true_lecturer, 'Java Script', 8)
best_student.rate(true_lecturer, 'Java Script', 10)
best_student.rate(true_lecturer, 'Java Script', 10)
best_student.rate(true_lecturer, 'C++', 6)
best_student.rate(true_lecturer, 'C++', 7)
best_student.rate(true_lecturer, 'C++', 10)

ever_better_student.rate(best_lecturer, 'Python', 10)
ever_better_student.rate(best_lecturer, 'Python', 8)
ever_better_student.rate(best_lecturer, 'Python', 9)
ever_better_student.rate(best_lecturer, 'Java Script', 5)
ever_better_student.rate(best_lecturer, 'Java Script', 9)
ever_better_student.rate(best_lecturer, 'Java Script', 9)
ever_better_student.rate(best_lecturer, 'C++', 9)
ever_better_student.rate(best_lecturer, 'C++', 2)
ever_better_student.rate(best_lecturer, 'C++', 7)
ever_better_student.rate(true_lecturer, 'Python', 9)
ever_better_student.rate(true_lecturer, 'Python', 8)
ever_better_student.rate(true_lecturer, 'Python', 9)
ever_better_student.rate(true_lecturer, 'Java Script', 8)
ever_better_student.rate(true_lecturer, 'Java Script', 10)
ever_better_student.rate(true_lecturer, 'Java Script', 10)
ever_better_student.rate(true_lecturer, 'C++', 6)
ever_better_student.rate(true_lecturer, 'C++', 7)
ever_better_student.rate(true_lecturer, 'C++', 10)

print('Оценки студентов по блокам: ' + '\n')
print(best_student.grades)                         # пуск
print(ever_better_student.grades)
print('\n\n')
print('Оценки лекторов по блокам: ' + '\n')
print(best_lecturer.grades)
print(true_lecturer.grades)
print('\n\n')
print('Статистика по студентам: ' + '\n')
print(best_student)
print(ever_better_student)
print('\n\n')
print('Статистика по лекторам: ' + '\n')
print(best_lecturer)
print(true_lecturer)
print('\n\n')
print('Преподаватели-практики: ' + '\n')
print(cool_mentor)
print((de_mentor))

# задание 4
course_control = input('Для какого курса считать средний балл студентов? ')
mark_list = []
for i in student_list:
   x = i.course_controle()           # вспомогательная переменная
   mark_list.append(x)
course_average = float('{:.3f}'.format(sum(mark_list)/len(mark_list)))
print(f"Средний балл студентов по курсу {course_control} - {course_average}")


mentor_control = input('Для какого курса считать средний балл преподавателей? ')
mark_lst = []
for i in lecturer_list:
   x = i.mentor_controle()           # вспомогательная переменная
   mark_list.append(x)
course_average = float('{:.3f}'.format(sum(mark_list)/len(mark_list)))
print(f"Средние оценки лекторов по курсу {mentor_control} - {course_average}")