class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Ім'я: {self.name}\nВік: {self.age}")


class Student(Person):
    def __init__(self, name: str, age: int, id: int):
        super().__init__(name, age)
        self.id = id

    def study(self, subject: str):
        print(f"Студент {self.name}-{self.id} навчається предмету {subject.title()}")

    def introduce(self):
        print(f"Ім'я: {self.name}\nВік: {self.age}\nID: {self.id}\nНазва класу: {__class__.__name__}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self, s):
        print(f"Викладач: {self.name} навчає {self.subject} студента {s.name}")

    def introduce(self):
        print(f"Ім'я: {self.name}\nВік: {self.age}\nПредмет, який викладає: {self.subject}\n"
              f"Назва класу: {__class__.__name__}")

class Employee(Person):
    def __init__(self, name, age, salary, specialty):
        super().__init__(name, age)
        self.salary = salary
        self.specialty = specialty

    def work(self):
        print(f"{self.name} працює на посаді {self.specialty} і заробляє {self.salary} гривень")

    def introduce(self):
        print(f"Ім'я: {self.name}\nВік: {self.age}\nПосада: {self.specialty}\nЗарплата: {self.salary}\n"
              f"Назва класу: {__class__.__name__}")



student1 = Student("Yaroslav", 20, 5)
student1.study("english")
student1.introduce()
print()

teacher1 = Teacher("Svitlana", 33, "Mathematics")
teacher1.teach(student1)
teacher1.introduce()
print()

employee1 = Employee("Wowa", 20, 20000, "Junior Python Developer")
employee1.work()
employee1.introduce()



