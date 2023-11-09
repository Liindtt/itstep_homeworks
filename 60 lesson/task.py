def init(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender


def greet(self):
    print(f"Hello, my name is {self.name}, I'm {self.age}")


def description(self):
    print(f"Person: {self.name}, {self.age}, {self.gender}")


attrs = {
    'team': "Python31",
    '__init__': init,
    'greet': greet,
    'description': description
}

Student = type('Student', (), attrs)

student = Student("Vadym", 36, "Male")
student.greet()
student.description()
