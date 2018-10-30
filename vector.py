from math import sqrt, fsum, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30
TOLERANCE = 1e-10

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return Vector([ a + b for a, b in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([ a - b for a, b in zip(self.coordinates, v.coordinates)])

    def __mul__(self, scalar):
        return Vector([ Decimal(scalar) * a for a in self.coordinates])

    __rmul__ = __mul__ # this tells python what method to use when 2 * vector is used

    def magnitude(self):
        """
        Magnitude represents the length of the vector
        """
        return Decimal(sqrt(sum([a ** 2 for a in self.coordinates])))


    def normalize(self):
        """
        This finds a unit vector (length 1) in the same direction as
        the given vector
        """
        try:
            return (Decimal('1.0') / self.magnitude()) * self
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        """
        a scalar

        This is an interpretation of how geometrically similar two vectors
        are to each other. Maybe their magnitudes are different, but the dot product
        is an interpretation of the ANGLE between them. Do they point in similar directions?

        If dot product is equal to ||v|| * ||w|| then angle between them is 0 (same direction)
        If dot product is equal to -||v|| * ||w|| then angle between them is 1 (opposite directions)
        If dot product is equal to 0 then angle between them is 90degrees pi/2 rads.
        """
        return sum([a * b for a,b in zip(self.coordinates, v.coordinates)])

    def angle(self, v, in_degrees = False):
        """
        returns the angle between two vectors
        We can do this by finding the normalization of V and dot it with the normalization of W
        """
        try:
            radians = acos(round(self.normalize().dot(v.normalize()), 10))
            return degrees(radians) if in_degrees else radians
        except Exception as e:
            raise e

    def is_zero(self):
        return self.magnitude() < TOLERANCE

    def is_parallel_to(self, v):
        """
        returns true if two vectors are parallel
        """
        return (self.is_zero() or v.is_zero() or self.angle(v) == 0 or self.angle(v) == pi)

    def is_orthogonal_to(self, v):
        """
        returns true if two vectors are orthogonal to each other (up to a tolerance)
        """
        return abs(self.dot(v)) < TOLERANCE

    def component_parallel_to(self, b):
        """
        a vector v is equal to its parallel component + its perpendicular component.

        this function finds the component of self in the direction of b (parallel to be).
        this component is parallel to b, but is also called the projection of self on to b.
        also known as "v parallel" or "v double bar"
        """
        unitB = b.normalize()
        return self.dot(unitB) * unitB

    def component_orthogonal_to(self, b):
        """
        returns the orthogonal component of the projection of self on to b
        also known as "v perp"
        """
        projection = self.component_parallel_to(b)
        return self - projection

    def cross(self, v):
        """
        returns the cross product of self and v.

        cross product only exists in 3 dimensions
        it's a vector that is orthogonal to both v and w, and has length mag v * mag w * sin(theta) between v and w

        There are two vectors that satisfy the cross product, each being opposite direction to each other.
        you can find which one is relevant by using the right hand rule (thumb in direction of v, index in direction of w
        then middle finger straight down)
        """
        if self.dimension != 3 or v.dimension != 3:
            raise Exception('Cross product only supports vectors in 3 dimensions')

        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates
        return Vector([(y1*z2 - y2 * z1), -(x1*z2 - x2*z1), (x1*y2 - x2*y1)])

    def parallelogram(self, v):
        return self.cross(v).magnitude()

    def triangle(self, v):
        return 0.5 * self.cross(v).magnitude()