""" Vector - an object that defines a vector """
from math import sqrt
class Vector(object):
    """ A Vector object

        constructor:
        coordinates -- an iterable
    """

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
            mutates the current vector
        """
        return tuple([
            x + y
            for (x, y) in zip(self.coordinates, vector.coordinates)
        ])


    def __sub__(self, vector):
        """ subtracts vector from the current vector
            mutates the current vector
        """
        return tuple([
            x - y
            for (x, y) in zip(self.coordinates, vector.coordinates)
        ])

    def __mul__(self, other):
        """ multiplies vector by scaling factor
            mutates the current vector
        """
        if isinstance(other, Vector):
            return tuple([
                x * y
                for (x, y) in zip(self.coordinates, other.coordinates)
            ])
        else:
            return tuple([
                other * x
                for x in self.coordinates
            ])

    def magnitude(self):
        """ returns the magnitude of the current vector """
        return sqrt(sum(x * x for x in self.coordinates))

    def normalize(self):
        """ returns normalized vector for the current vector """
        try:
            return Vector(self * (1./self.magnitude()))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
