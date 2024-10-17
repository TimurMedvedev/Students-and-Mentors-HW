import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.general_middle_grade = 0.0
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = {}
        

    def __str__ (self):
        if self.grades:
            string = f"Студент: \nИмя: {self.name} \nФамилия: {self.surname} \nCредняя оценка: {self.middle_grade} \nОбщая средняя оценка: {self.general_middle_grade}\n"
        else:
            string = f"Студент: \nИмястудента: {self.name} \nФамилия: {self.surname} \nCтудент не получал оценок\n"
        return string
    
    def __eq__(self, other):
        
        if self.general_middle_grade == other.general_middle_grade:
            return "Успеваемость одинаковая!\n"
        elif self.general_middle_grade > other.general_middle_grade:
            string = f"Успеваемость Ученика {self.name} лучше чем у {other.name}!\n"
            return string
        else:
            string =  f"Успеваемость Ученика {other.name} лучше чем у {self.name}!\n"
            return string
    
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades_for_lections:
                lecturer.grades_for_lections[course] += [grade]
            else:
                lecturer.grades_for_lections[course] = [grade]
        else:
            return 'Ошибка'
        lecturer.middle_grade_lec [course] = statistics.mean(lecturer.grades_for_lections[course])
      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__( name, surname)
        self.grades_for_lections = {}
        self.middle_grade_lec = {}
    
    def __str__ (self):
        if self.grades_for_lections:
            string = f"Лектор: \nИмя: {self.name} \nФамилия: {self.surname} \nCредняя оценка: {self.middle_grade_lec}\n"
        else:
            string = f"Лектор: \nИмя: {self.name} \nФамилия: {self.surname} \nCтудент не получал оценок\n"
        return string
     
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def __str__(self):
        string = f"Эксперт, проверяющий задание: \nИмя: {self.name} \nФамилия: {self.surname}\n"
        return string
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        student.middle_grade[course] = statistics.mean(student.grades[course])

    def general_middle_grade(self, student):
        i = 0
        if isinstance (student, Student):
            if student.general_middle_grade == 0:
                student.general_middle_grade = student.middle_grade[student.courses_in_progress[0]]
            else:
                for course in student.courses_in_progress:
                    student.general_middle_grade = (student.general_middle_grade + student.middle_grade[student.courses_in_progress[i]])/2
                    i += 1
        
student1 = Student("Harry", "Potter", "Male")
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student2 = Student("Hermione", "Granger", "Female")
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']

lecturer1 = Lecturer("John", "Constantine")
student1.rate_lec(lecturer1, "Python", 8)
student2.rate_lec(lecturer1, "Python", 10)

lecturer2 = Lecturer("Merlin", "The Wizard")
student1.rate_lec(lecturer2, "Git", 7)
student2.rate_lec(lecturer2, "Git", 10)

reviewer1 = Reviewer("Butcher", "The First")
reviewer1.rate_hw(student1, "Python", 7)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student2, "Python", 10)
reviewer1.rate_hw(student2, "Python", 10)
reviewer1.general_middle_grade(student1)
reviewer1.general_middle_grade(student2)

reviewer2 = Reviewer("Butcher", "The Second")
reviewer1.rate_hw(student1, "Git", 7)
reviewer1.rate_hw(student1, "Git", 9)
reviewer1.rate_hw(student2, "Git", 10)
reviewer1.rate_hw(student2, "Git", 10)
reviewer2.general_middle_grade(student1)
reviewer2.general_middle_grade(student2)

print(student1)
print(student2)
print(student1 == student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)


