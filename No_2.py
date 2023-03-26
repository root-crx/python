class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0 , "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f'学生{self.name} (学号: {self.student_id}) 的成绩为: ')
        for course in self.grades:
            print(f'{course}: {self.grades[course]}分')

daming = Student('Daming', '10000')
daming.set_grade('语文', 96)
daming.set_grade('数学', 99)
daming.set_grade('英语', 98)
daming.print_grades()
# 学生成绩显示
