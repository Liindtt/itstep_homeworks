class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def __repr__(self):
        return f"repr {self.name} - {self.scores}"

    # def __str__(self):
    #     return f"str {self.name} - {self.scores}"

    def __getitem__(self, index):
        return self.scores[index]

    def __setitem__(self, index, value):
        self.scores[index] = value

    def __delitem__(self, index):
        print(f"Виконується видалення по індексу {index}")
        del self.scores[index]

    def __call__(self, semestr=""):
        print(f"Виклик на сесію - {semestr}")

    def __getattr__(self, item):
        print(f"get attribute")
        return None

    def __getattribute__(self, item):
        print(f"get attribute name")
        if item == "name":
            return 5


A = Student("Alice", [5, 6, 8, 12])
print(A.age)

#
# print(A)
# A[0] = 12
# print(A)
# del A[0]
# print(A)
# A("III")
# A()
