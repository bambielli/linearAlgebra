""" Main Function """
from vector import Vector

QUIZ_VECTOR_1 = Vector([8.218, -9.341])
QUIZ_VECTOR_2 = Vector([-1.129, 2.111])

# print(QUIZ_VECTOR_1 + QUIZ_VECTOR_2)

QUIZ_VECTOR_3 = Vector([7.119, 8.215])
QUIZ_VECTOR_4 = Vector([-8.223, 0.878])

# print(QUIZ_VECTOR_3 - QUIZ_VECTOR_4)

QUIZ_VECTOR_5 = Vector([1.671, -1.012, -0.318])
SCALAR = 7.41

# print(QUIZ_VECTOR_5 * SCALAR)

TEST_VECTOR = Vector([3, 4])
# print(TEST_VECTOR.magnitude())

MAG_QUIZ_1 = Vector([-0.221, 7.437])
MAG_QUIZ_2 = Vector([8.813, -1.331, -6.247])

# print(MAG_QUIZ_1.magnitude())
# print(MAG_QUIZ_2.magnitude())

MAG_QUIZ_3 = Vector([5.581, -2.136])
MAG_QUIZ_4 = Vector([1.996, 3.108, -4.554])

# print(MAG_QUIZ_3.normalize())
# print(MAG_QUIZ_4.normalize())


DOT_QUIZ_1A = Vector([7.887, 4.138])
DOT_QUIZ_1B = Vector([-8.802, 6.776])
# print(DOT_QUIZ_1A.dot(DOT_QUIZ_1B))

DOT_QUIZ_2A = Vector([-5.955, -4.904, -1.874])
DOT_QUIZ_2B = Vector([-4.496, -8.755, 7.103])
# print(DOT_QUIZ_2A.dot(DOT_QUIZ_2B))

DOT_QUIZ_3A = Vector([3.183, -7.627])
DOT_QUIZ_3B = Vector([-2.668, 5.319])
# print(DOT_QUIZ_3A.angle(DOT_QUIZ_3B))

DOT_QUIZ_4A = Vector([7.35, 0.221, 5.188])
DOT_QUIZ_4B = Vector([2.751, 8.259, 3.985])
# print(DOT_QUIZ_4A.angle(DOT_QUIZ_4B, True))



PARALLEL_ORTH_1A = Vector([-7.579, -7.88])
PARALLEL_ORTH_1B = Vector([22.737, 23.64])
# print("parallel: " + str(PARALLEL_ORTH_1A.is_parallel_to(PARALLEL_ORTH_1B)))
# print("orth: " + str(PARALLEL_ORTH_1A.is_orthogonal_to(PARALLEL_ORTH_1B)))

PARALLEL_ORTH_2A = Vector([-2.029, 9.97, 4.172])
PARALLEL_ORTH_2B = Vector([-9.231, -6.639, -7.245])
# print("parallel: " + str(PARALLEL_ORTH_2A.is_parallel_to(PARALLEL_ORTH_2B)))
# print("orth: " + str(PARALLEL_ORTH_2A.is_orthogonal_to(PARALLEL_ORTH_2B)))

PARALLEL_ORTH_3A = Vector([-2.328, -7.284, -1.214])
PARALLEL_ORTH_3B = Vector([-1.821, 1.072, -2.94])
# print("parallel: " + str(PARALLEL_ORTH_3A.is_parallel_to(PARALLEL_ORTH_3B)))
# print("orth: " + str(PARALLEL_ORTH_3A.is_orthogonal_to(PARALLEL_ORTH_3B)))

PARALLEL_ORTH_4A = Vector([2.118, 4.827])
PARALLEL_ORTH_4B = Vector([0, 0])
# print("parallel: " + str(PARALLEL_ORTH_4A.is_parallel_to(PARALLEL_ORTH_4B)))
# print("orth: " + str(PARALLEL_ORTH_4A.is_orthogonal_to(PARALLEL_ORTH_4B)))

PROJ_1A = Vector([3.039, 1.879])
PROJ_1B = Vector([0.825, 2.036])
# print(PROJ_1A.projection(PROJ_1B))

PROJ_2A = Vector([-9.88, -3.264, -8.159])
PROJ_2B = Vector([-2.155, -9.353, -9.473])
# print(PROJ_2A.orthogonal(PROJ_2B))

PROJ_3A = Vector([3.009, -6.172, 3.692, -2.51])
PROJ_3B = Vector([6.404, -9.144, 2.759, 8.718])
# print(PROJ_3A.projection(PROJ_3B))
# print(PROJ_3A.orthogonal(PROJ_3B))


CROSS_1A = Vector([8.462, 7.893, -8.187])
CROSS_1B = Vector([6.984, -5.975, 4.778])
print(CROSS_1A.cross(CROSS_1B))

CROSS_2A = Vector([-8.987, -9.838, 5.031])
CROSS_2B = Vector([-4.268, -1.861, -8.866])
print(CROSS_2A.parallelogram(CROSS_2B))

CROSS_3A = Vector([1.5, 9.547, 3.691])
CROSS_3B = Vector([-6.007, 0.124, 5.772])
print(CROSS_3A.triangle(CROSS_3B))