class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.l_course_attached = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
        return self.middle_rate_s() < other.middle_rate_s()

    def stud_rate(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.l_course_attached and course in lecture.courses_in_progress:
            if course in lecture.stud_grades:
                lecture.stud_grades[course] += [grade]
            else:
                lecture.stud_grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_rate_s(self):
        sum = 0
        quantity = 0
        if len(self.grades) != 0:
            for val in self.grades.values():
                for grade in val:
                    sum += grade
                    quantity += 1
            average = round(sum / quantity, 1)
            return average
        else:
            return 'У студента еще нет оценок!'

    def __str__(self):
        res = f'\nИмя: = {self.name} ' \
              f'\nФамилия: = {self.surname} ' \
              f'\nСредняя оценка за домашние задания: {self.middle_rate_s()} ' \
              f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
              f'\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.stud_grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a student!')
        return self.middle_rate_l() < other.middle_rate_l()

    def middle_rate_l(self):
        sum = 0
        quantity = 0
        if len(self.stud_grades) != 0:
            for val in self.stud_grades.values():
                for grade in val:
                    sum += grade
                    quantity += 1
            average = round(sum / quantity, 1)
            return average
        else:
            return 'У лектора еще нет оценок!'

    def __str__(self):
        res = f'\nИмя: = {self.name} ' \
              f'\nФамилия: = {self.surname} ' \
              f'\nСредняя оценка за лекции: {self.middle_rate_l()}\n '
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'\nИмя: {self.name} ' \
              f'\nФамилия: {self.surname}\n'
        return res

# Расчет средней оценки всех студентов
course = 'Python'

def middle_rate_student(student_list, course):
  sum_grades = 0
  len_grades = 0
  for student in student_list:
      if course in student.courses_in_progress:
          if course in student.grades:
            sum_grades += sum(student.grades[course])
            len_grades += len(student.grades[course])
  average = round(sum_grades / len_grades, 2)
  return f'\nСредняя оценка студентов за курс {course}: {average}'


# Расчет средней оценки всех лекторов
lecture_course = 'Python'

def middle_rate_lecture(lecture_list, lecture_course):
  sum_grades = 0
  len_grades = 0
  for lecture in lecture_list:
      if lecture_course in lecture.courses_in_progress:
          if lecture_course in lecture.stud_grades:
            sum_grades += sum(lecture.stud_grades[lecture_course])
            len_grades += len(lecture.stud_grades[lecture_course])
  average = round(sum_grades / len_grades, 2)
  return f'Средняя оценка лекторов за курс {lecture_course}: {average}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.l_course_attached += ['Python']

best_student_2 = Student('Ruoy_2', 'Eman_2', 'your_gender')
best_student_2.courses_in_progress += ['Python', 'Git']
best_student_2.finished_courses += ['Введение в программирование']
best_student_2.l_course_attached += ['Python']
student_list = [best_student, best_student_2]

best_lecture = Lecturer('Some', 'Buddy')
best_lecture.courses_in_progress += ['Python']
best_lecture_2 = Lecturer('Some_3', 'Buddy_3')
best_lecture_2.courses_in_progress += ['Python']
lecture_list = [best_lecture, best_lecture_2]

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 6)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)

best_student.stud_rate(best_lecture, 'Python', 10)
best_student.stud_rate(best_lecture, 'Python', 9)
best_student.stud_rate(best_lecture, 'Python', 8)
best_student.stud_rate(best_lecture_2, 'Python', 10)
best_student.stud_rate(best_lecture_2, 'Python', 2)
best_student.stud_rate(best_lecture_2, 'Python', 4)

print(cool_reviewer)
print(best_student)
print(best_student_2)
print(best_lecture)
print(best_lecture_2)
print(best_student < best_student_2)
print(best_lecture < best_lecture_2)
print(middle_rate_student(student_list, course))
print(middle_rate_lecture(lecture_list, lecture_course))


