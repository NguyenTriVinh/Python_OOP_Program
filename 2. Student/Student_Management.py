class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        if self.courses:
            print('Course: ')
            for i in self.courses:
                print(f" + {i}")

student1 = Student('Join', 'S001')

student1.add_course('OOP')
student1.add_course('DSA')

student1.print_info()


