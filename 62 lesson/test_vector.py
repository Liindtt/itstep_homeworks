from vector import Vector
import pytest
from math import sqrt

@pytest.fixture
def create_vector():
    return Vector(9, 6, 3)

# test equal method
def test_eq(create_vector):
    obj_vector = create_vector
    assert obj_vector == Vector(9, 6, 3)    # True
    # assert obj_vector == Vector(3, 6, 9)  # False

# test vector's length
def test_length(create_vector):
    obj_vector = create_vector
    assert Vector.length(obj_vector) == sqrt((obj_vector.x ** 2 + obj_vector.y ** 2 + obj_vector.z ** 2))

# test whole part of vector's length
def test_int(create_vector):
    obj_vector = create_vector
    assert int(Vector.length(obj_vector)) == int(sqrt((obj_vector.x ** 2 + obj_vector.y ** 2 + obj_vector.z ** 2)))

# test the addition of two vectors
def test_add(create_vector):
    new_obj = create_vector + Vector(3, 6, 9)
    assert create_vector != new_obj
    assert new_obj == Vector(12, 12, 12)

# test the multiple vector on number
def test_mul(create_vector):
    new_obj = create_vector * 5
    assert new_obj == Vector(create_vector.x * 5, create_vector.y * 5, create_vector.z * 5)
    assert new_obj == Vector(45, 30, 15)

# test -= of two vectors
def test_isub(create_vector):
    vector1 = Vector(20, 10, 5)
    vector2 = Vector(15, 5, 0)
    vector1 -= vector2
    assert vector1 == Vector(5, 5, 5)
