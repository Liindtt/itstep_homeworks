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

def test_neg(create_vector):
    obj_vector = create_vector
    assert -obj_vector == Vector(obj_vector.x, obj_vector.y, obj_vector.z)




