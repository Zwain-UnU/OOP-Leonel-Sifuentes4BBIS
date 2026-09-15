class Student:
    def __init__(self,name):
        self.name = name

    def enroll(self, course):
        self.course = course
    def show_course(self):
        print(f"{self.name} is enrolled in {self.course.name}")

class Course:
    def __init__(self, name):
        self.name = name

#Instances 

student = Student("Carlos")
course = Course("Python Programming")

#Creating a relationship
student.enroll(course)

#Output expected :"Carlos is enrolled in Python Programming")
