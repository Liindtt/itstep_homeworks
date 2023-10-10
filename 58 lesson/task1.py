class Size:
    def __get__(self, instance, owner):
        return len(instance.name)

class Person:
    size_name = Size()  # Descriptor instance

    def __init__(self, name):
        self.name = name


person1 = Person("Evelina")
print(f"Довжина імені `{person1.name}` = {person1.size_name}")
