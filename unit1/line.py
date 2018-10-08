from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output
    
    def __eq__(self, line):
        """
        To find if two lines are equal, find a point on each line, then find the vector connecting those points.
        if that vector is orthogonal to the normal vectors of each line, then the lines are equal.
        """
        if self.normal_vector.is_zero():
            if not line.normal_vector.is_zero():
                # if only one line is zero, they are not equivalent
                return False
            else:
                # if the second line is also zero, they are equivalently zero
                diff = self.constant_term - line.constant_term
                return MyDecimal(diff).is_near_zero()
        elif line.normal_vector.is_zero():
            # only one line is zero if we get here (the second line)
            return False
        
        # get basepoints of both lines
        b1 = self.basepoint
        b2 = line.basepoint

        # to find the vector connecting two points, subtract the vector representation of both points.
        # I had no idea this was a way to find the vector connecting two points.
        diff = b1 - b2 #this is a vector

        # if the line is orthogonal to both normal vectors of the lines in question, they are the same line.
        return diff.is_orthogonal_to(self.normal_vector) and diff.is_orthogonal_to(line.normal_vector)


    @staticmethod
    def first_nonzero_index(iterable):
        count = 0
        for item in iterable:
            if not MyDecimal(item).is_near_zero():
                return count
            else:
                count += 1
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)
    
    def is_parallel_to(self, line):
        """
        if normal vectors are parallel, then the lines are parallel
        """
        import pdb
        pdb.set_trace()
        return self.normal_vector.is_parallel_to(line.normal_vector)


    def intersection(self, line):
        # check if parallel, return nothing
        # check if equal, return infinity
        if self.is_parallel_to(line):
            return None
        elif self == line:
            return self
        else:
            A, B = self.normal_vector.coordinates
            C, D = line.normal_vector.coordiantes
            k1 = self.constant_term
            k2 = self.constant_term
            x_numerator = D*k1 - B*k2
            y_numerator = -C*k1 + A*k2
            one_over_denom = Decimal('1')/(A*D - B*C)
            return Vector([x_numerator, y_numerator]) * one_over_denom

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps