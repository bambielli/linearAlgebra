from line import Line
from vector import Vector
from decimal import Decimal

QUIZ_LINE_1 = Line(Vector([Decimal(4.046), Decimal(2.836)]), Decimal(1.21))
QUIZ_LINE_2 = Line(Vector([Decimal(10.115), Decimal(7.09)]), Decimal(3.025))

print(QUIZ_LINE_1.is_parallel_to(QUIZ_LINE_2))
print(QUIZ_LINE_1 == QUIZ_LINE_2)
print(QUIZ_LINE_1.intersection(QUIZ_LINE_2))

QUIZ_LINE_3 = Line(Vector([Decimal(7.204), Decimal(3.182)]), Decimal(8.68))
QUIZ_LINE_4 = Line(Vector([Decimal(8.172), Decimal(4.114)]), Decimal(9.883))

print(QUIZ_LINE_3.is_parallel_to(QUIZ_LINE_4))
print(QUIZ_LINE_3 == QUIZ_LINE_4)
print(QUIZ_LINE_3.intersection(QUIZ_LINE_4))

QUIZ_LINE_5 = Line(Vector([Decimal(1.182), Decimal(5.562)]), Decimal(6.744))
QUIZ_LINE_6 = Line(Vector([Decimal(1.773), Decimal(8.343)]), Decimal(9.525))

print(QUIZ_LINE_5.is_parallel_to(QUIZ_LINE_6))
print(QUIZ_LINE_5 == QUIZ_LINE_6)
print(QUIZ_LINE_5.intersection(QUIZ_LINE_6))