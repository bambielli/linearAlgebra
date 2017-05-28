""" Vector - an object that defines a vector """
from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 4

class Vector(object):
    """ A Vector object

        constructor:
        coordinates -- an iterable
    """
    cannot_normalize_zero_vector = "Cannot normalize the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, vector):
        """ adds vector to the current vector
            returns a new vector
        """
        return tuple([
            x + y
            for (x, y) in zip(self.coordinates, vector.coordinates)])


    def __sub__(self, vector):
        """ subtracts vector from the current vector
            returns a new vector
        """
        return tuple([
            x - y
            for (x, y) in zip(self.coordinates, vector.coordinates)])

    def __mul__(self, scalar):
        """ multiplies vector by scaling factor
            returns a new vector
        """
        return tuple([
            Decimal(scalar)*x
            for x in self.coordinates])

    def magnitude(self):
        """ returns the magnitude of the current vector

            magnitude is a value that indicates how much distance the vector covers
        """
        return Decimal(sqrt(sum(x**2 for x in self.coordinates)))

    def normalize(self):
        """ returns normalized vector for the current vector

            normalized vector is the unit vector that is in the same direction
            as the given vector. Unit vector is vector of magnitude 1 in a given direction
        """
        try:
            magnitude = self.magnitude()
            return Vector(self * (Decimal('1.0')/magnitude))
        except ZeroDivisionError:
            raise ZeroDivisionError(self.cannot_normalize_zero_vector)

    def dot(self, vector):
        """ returns the dot product of the two vectors

            dot product allows us to find the angle between two vectors
        """
        return sum(x * y for x, y in zip(self.coordinates, vector.coordinates))

    def angle(self, vector, in_degrees=False):
        """ returns the angle between the two vectors """
        # rad_val = acos(self.dot(vector) / (self.magnitude() * vector.magnitude()))
        try:
            norm_1 = self.normalize()
            norm_2 = vector.normalize()
            rad_val = acos(norm_1.dot(norm_2))
            print(rad_val)
            if in_degrees:
                return degrees(rad_val)
            else:
                return rad_val
        except ZeroDivisionError:
            raise Exception("Cannot compute angle with the zero vector")

    def is_parallel_to(self, vector):
        """ returns a boolean indicating if the two vectors are parallel
            true when the vectors are scalar multiples of each other
        """
        # try:
        #     scalar_list = [
        #         x / y
        #         for x, y in zip(self.coordinates, vector.coordinates)
        #     ]
        #     return len(set(scalar_list)) == 1
        # except ZeroDivisionError:
        #     return True
        return (self.is_zero() or
                vector.is_zero() or
                self.angle(vector) == 0 or
                self.angle(vector) == pi)

    def is_orthogonal_to(self, vector, tolerance=1e-10):
        """ returns a boolean indicating if the two vectors are orthogonal
            true when dot product between two vectors is 0
            (which indicates that the cos of the angle between them is 0)
        """
        return abs(self.dot(vector)) < tolerance

    def is_zero(self, tolerance=1e-10):
        """ returns a boolean indicating whether the vector is zero (to a tolerance)
            We know a vector is zero when its magnitude is zero
        """

        return self.magnitude() < tolerance
