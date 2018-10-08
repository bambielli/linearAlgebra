""" Vector - an object that defines a vector """
from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 10

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
            self.i = 0

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
        return Vector([
            x + y
            for (x, y) in zip(self.coordinates, vector.coordinates)])


    def __sub__(self, vector):
        """ subtracts vector from the current vector
            returns a new vector
        """
        return Vector([
            x - y
            for (x, y) in zip(self.coordinates, vector.coordinates)])

    def __mul__(self, scalar):
        """ multiplies vector by scaling factor
            returns a new vector
        """
        return Vector([
            Decimal(scalar)*x
            for x in self.coordinates])

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.coordinates):
            coord = self.coordinates[self.i]
            self.i += 1
            return coord
        else:
            raise StopIteration()
    
    def __getitem__(self, index):
        return self.coordinates[index]

    def magnitude(self):
        """ returns the magnitude of the current vector

            magnitude is a value that indicates how much distance the vector covers
            also referred to as the "length" of the vector
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
        return Decimal(sum(x * y for x, y in zip(self.coordinates, vector.coordinates)))

    def angle(self, vector, in_degrees=False):
        """ returns the angle between the two vectors """
        # rad_val = acos(self.dot(vector) / (self.magnitude() * vector.magnitude()))
        try:
            norm_1 = self.normalize()
            norm_2 = vector.normalize()
            rad_val = acos(norm_1.dot(norm_2))
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

    def projection(self, basis):
        """ returns the projection of the vector on to the given basis vector """
        try:
            unit_b = basis.normalize()
            scale = self.dot(unit_b)
            return unit_b * scale
        except ZeroDivisionError:
            raise ZeroDivisionError("no component parallel to zero vector")

    def orthogonal(self, basis):
        """ returns the component of the vector orthogonal to the given basis vector """
        try:
            proj_v = Vector(self.projection(basis))
            return self - proj_v
        except ZeroDivisionError:
            raise Exception("No component orthogonal to zero vector")

    def cross(self, vector):
        """ returns a vector that represents the cross product of the given vectors
            Cross product is the vector that is orthogonal to both given vectors in 3d space
        """
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = vector.coordinates
            cross = [y1 * z2 - y2 * z1,
                     -(x1 * z2 - x2 * z1),
                     x1 * y2 - x2 * y1]
            return Vector(cross)
        except ValueError:
            raise Exception("Cross product requires vectors in 3 dimensions")

    def parallelogram(self, vector):
        """ returns the area of the paralellogram that is created by the given vectors
            This is calculated by taking the magnitude of the cross product of the given vectors
        """

        cross = self.cross(vector)
        return cross.magnitude()

    def triangle(self, vector):
        """ returns the area of the triangle created by given vectors
            This is calculated by taking 1/2 the magnitude of the cross product
        """

        cross = self.cross(vector)
        return Decimal(0.5) * cross.magnitude()
