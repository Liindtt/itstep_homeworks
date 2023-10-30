from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def fill_color(self, color: str):
        pass

    @abstractmethod
    def erase(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Малюємо круг")

    def fill_color(self, color: str):
        print(f"Наповнюємо круг {color.replace('й', 'м')} кольором")

    def erase(self):
        print("Стираємо круг")


class Rectangle(Shape):
    def draw(self):
        print("Малюємо квадрат")

    def fill_color(self, color: str):
        print(f"Наповнюємо квадрат {color.replace('й', 'м')} кольором")

    def erase(self):
        print("Стираємо квадрат")


class Create(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def render(self):
        figure = self.create_product()
        color = input("Введіть бажаний колір: ")
        figure.fill_color(color=color)
        figure.draw()


class CreateCircle(Create):
    def create_product(self):
        print("Створюємо круг")
        return Circle()


class CreateRectangle(Create):
    def create_product(self):
        print("Створюємо квадрат")
        return Rectangle()


create_cir = CreateCircle()
create_cir.render()
print()

create_rect = CreateRectangle()
create_rect.render()
