""" Main Function """
from vector import Vector

QUIZ_VECTOR_1 = Vector([8.218, -9.341])
QUIZ_VECTOR_2 = Vector([-1.129, 2.111])

QUIZ_VECTOR_1 + QUIZ_VECTOR_2
print(QUIZ_VECTOR_1)

QUIZ_VECTOR_3 = Vector([7.119, 8.215])
QUIZ_VECTOR_4 = Vector([-8.223, 0.878])

QUIZ_VECTOR_3 - QUIZ_VECTOR_4
print(QUIZ_VECTOR_3)

QUIZ_VECTOR_5 = Vector([1.671, -1.012, -0.318])
SCALAR = 7.41

QUIZ_VECTOR_5 * SCALAR
print(QUIZ_VECTOR_5)

TEST_VECTOR = Vector([3, 4])
print(TEST_VECTOR.magnitude())

MAG_QUIZ_1 = Vector([-0.221, 7.437])
MAG_QUIZ_2 = Vector([8.813, -1.331, -6.247])

print(MAG_QUIZ_1.magnitude())
print(MAG_QUIZ_2.magnitude())

MAG_QUIZ_3 = Vector([5.581, -2.136])
MAG_QUIZ_4 = Vector([1.996, 3.108, -4.554])

print(MAG_QUIZ_3.normalize())
print(MAG_QUIZ_4.normalize())