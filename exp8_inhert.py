class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = Person(name, age)
print("\nPerson Details:")
person.display()  

student_id = input("\nEnter your student ID: ")
course = input("Enter your course name: ")

student = Student(name, age, student_id, course)
print("\nStudent Details:")
student.display()  