class Point:

    """Class Point 2D"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Point(new_x, new_y)
        elif isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y + other
            return Point(new_x, new_y)
        else:
            raise TypeError("Невірний тип операнда")

    def __radd__(self, other):      # 5 + A: self = A, other = 5
        return self.__add__(other)

    def __len__(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    A = Point(1, 3)
    B = Point(2, 3)
    print(A)
    print(B)
    print(A == B)
    C = 5 + A
    print(C, type(C))
    print(f"len A = {len(A)}")




