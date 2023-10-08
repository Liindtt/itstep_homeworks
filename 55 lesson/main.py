from math import sqrt

class Vector:
    def __init__(self, x, y, z):
        # checking coordinates for digital data type
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
            raise TypeError(f"parameter must be of either `int` or `float` type")
        self.x = x
        self.y = y
        self.z = z

    # print coordinates of vector
    def __str__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    # override == method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # override + method
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # override - method
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # override += method
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    # override -= method
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    # override * method
    def __mul__(self, other):
        if isinstance(self, Vector) and isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(self, Vector) and isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("arguments or vectors must have integer type")

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    # get vector's length
    def length(self):
        return sqrt((self.x ** 2 + self.y ** 2 + self.z ** 2))

    # returning a whole part of vector's length
    def __int__(self):
        return int(self.length())

    # transformation vector's args to negative
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    # get value by key
    def __getitem__(self, item):
        if item == 1:
            return self.x
        elif item == 2:
            return self.y
        elif item == 3:
            return self.z
        else:
            raise IndexError("that index does not exist")

    # set a new value by key
    def __setitem__(self, key, value):
        if key == 1:
            self.x = value
        elif key == 2:
            self.y = value
        elif key == 3:
            self.z = value
        else:
            raise IndexError("that index does not exist")

    # check if item equal one of vector's args
    def __contains__(self, item):
        if self.x == item or self.y == item or self.z == item:
            return True

    # returning true if vector's length != 0
    def __bool__(self):
        if self.length() != 0:
            return True
        else:
            return False

    # returning functor with some args
    def __call__(self, *args):
        p = "Functor with arguments: "
        for arg in args:
            p += str(arg)
        return p


v1 = Vector(1, 2, 3)
v2 = Vector(1, 2, 3)
v3 = Vector(3, 2, 1)
v4 = Vector(0, 0, 0)
print(v1)

# 1. comparing two vectors
print(v1 == v2)
print(v1 != v3)
print()

# 2. addition and subtraction two vectors
print(v1 + v3)
print(v1 - v3)
print()

# 3. addition and subtraction with assignment
v1 += v3
print(v1)
v1 -= v3
print(v1)
print()

# 4. scalar product both vectors
v9 = v1 * v3
print(v9)

# 5. product digit on vector
v3 *= 3
print(v3)
v2 = v2 * 5
print(v2)
v2 = 2.5 * v2
print(v2)
print()

# 6. length of vector
print(v1.length())
print()

# 7. whole part of vector
print(int(v1))
print()

# 8. returning negative
print(v2)
print(-v2)
print()

# 9. returning and changing vector's value
print(v2)
v2[3] = 30
print(v2[3])
print(v2)
print()

# 10. returning bool value by result
print(v1)
print(2 in v1)
print(5 in v1)
print()

# 11. returning True if vector's length not equal 0
print(v4)
print(v4.length())
print(bool(v4))
print(v1)
print(v1.length())
print(bool(v1))
print()

# 12. calling a functor
print(v2(v2, v2.length()))
