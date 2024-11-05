class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

person1 = Person(name, age)

person1.greet()
