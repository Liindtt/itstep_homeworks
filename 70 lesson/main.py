from abc import ABC, abstractmethod
from math import pi

class IShape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

class Shape(IShape):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def info(self):
        pass

class Pizza(Shape):
    def __init__(self,  name: str, price: float, shape: IShape,):
        super().__init__(name)
        self.price = price
        self.shape = shape

    def get_price(self):
        return self.price

    def get_shape_class(self):
        return self.shape.name

    def get_area(self) -> float:
        pass

    def cut_pizza(self):
        pass

    def info(self):
        print(f"Піца: {self.name}, Ціна: {pizza.get_price()}, Форма: {pizza.get_shape_class()}")


class Square(Shape):
    def __init__(self, name: str, side: float):
        super().__init__(name)
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2

    def info(self):
        print(f"{self.name}, Довжина сторони: {self.side}, Площа: {self.get_area()}см²")

class Circle(Shape):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2

    def info(self):
        print(f"{self.name}, Радіус: {self.radius}, Площа: {self.get_area()}см²")


square = Square("Квадрат", 5.0)
circle = Circle("Круг", 3.0)
pizza = Pizza("Гаваї", 58.5, circle)

# print(f"{square.name}, Площа: {square.get_area()}")
# print(f"{circle.name}, Площа: {circle.get_area()}")
# print(f"Піца:\n\tЦіна: {pizza.get_price()},\n\tФорма: {pizza.get_shape_class()}")
square.info()
circle.info()
pizza.info()
