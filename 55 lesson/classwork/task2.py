from task1 import Point
from math import pi, trunc

class Circle:
    def __init__(self, r, x=0, y=0):
        self.radius = r
        self.point = Point(x, y)

    def __repr__(self):
        return f"Circle radius {self.radius}, with point {self.point}"

    def __eq__(self, other):
        return self.radius == other.radius and self.point == other.point

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.radius >= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __iadd__(self, other):
        # return Circle(self.radius + other, self.point.x, self.point.y)
        self.radius += other
        return self

    def __int__(self):
        l = 2 * pi * self.radius
        return trunc(l)

    def __len__(self):
        return self.__int__()


c1 = Circle(2, 0, 0)
c2 = Circle(2, 0, 0)
print(c1)
print(c2)

print(c1 == c2)
print(c1 != c2)
print(c1 >= c2)
print(c1 < c2)

print()
print(c1, id(c1))
c1 += 5
print(c1, id(c1))

print(len(c1))
