""" Vector - an object that defines a vector """
import math
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
        self.coordinates = tuple([
            round(x + y, 3)
            for (x, y) in zip(self.coordinates, vector.coordinates)
        ])


    def __sub__(self, vector):
        """ subtracts vector from the current vector
            mutates the current vector
        """
        self.coordinates = tuple([
            round(x - y, 3)
            for (x, y) in zip(self.coordinates, vector.coordinates)
        ])

    def __mul__(self, other):
        """ multiplies vector by scaling factor
            mutates the current vector
        """
        if isinstance(other, Vector):
            self.coordinates = tuple([
                round(x * y, 3)
                for (x, y) in zip(self.coordinates, other.coordinates)
            ])
        else:
            self.coordinates = tuple([
                round(other * x, 3)
                for x in self.coordinates
            ])
    def multiply(self, other):
        """ returns new vector """
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
        return math.sqrt(math.fsum(x*x for x in self.coordinates))

    def normalize(self):
        """ returns normalized vector for the current vector """

        my_vec = Vector(self.multiply(1 / self.magnitude()))
        print(sum(x*x for x in my_vec.coordinates))
        return my_vec
