from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30

class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        """
        mutating operation
        """
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        """
        mutating operation. Implemented __mul__ and __rmul__ in Plane class
        """
        self.planes[row] = coefficient * self.planes[row]

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        multiplied_row = coefficient * self.planes[row_to_add]
        to_be_added_to = self.planes[row_to_be_added_to]
        new_row = Plane(
          normal_vector=to_be_added_to.normal_vector + multiplied_row.normal_vector,
          constant_term=to_be_added_to.constant_term + multiplied_row.constant_term
          )
        self.planes[row_to_be_added_to] = new_row

    def compute_triangular_form(self):
      """
      computes triangular form with the following rules:
      1) swaps occur from the first qualifying equation that is found
      2) no multiplication of equations is allowed

      This works by first through each variable in the dimension space
      e.g. if 3 dimensions, will look for x, y, and z in indices
      and checking if it needs to be eliminated in the n+1 equations below its spot.
      """
      system = deepcopy(self)
      indices = system.indices_of_first_nonzero_terms_in_each_row()

      # range is [0, 1, 2...] this means triangular
      for ind in range(len(indices[:self.dimension])):
        ind_value = indices[ind]
        # check to see if there is a value of ind in the ith place in spliced indices
        if ind != ind_value and ind_value != -1:
          try:
            swap_from = indices.index(ind)
            swap_to = ind
            system.swap_rows(swap_from, swap_to)
            # at this point we can guarantee that there is an eq with leading term ind_value
            # in the ind position in the planes array in system.
            # but we also need to re-calculate the indices, since swaps happened
            indices = system.indices_of_first_nonzero_terms_in_each_row()
          except ValueError:
            # this happens when we can't find an index with the value ind as a leading term in any equation.
            # if that is the case, we shouldn't try to do any more elimination,
            # since that variable has already been sufficiently eliminated in our system.
            # e.g x + y + z = 1 (no leading y)     or    y + z = 1   (since there is no leading x)
            #             z = 2                          2y + 2z = 2
            # We should just continue to check the next variable in the system.
            continue

        # perform elimination against each other equation, if necessary
        for dex, dex_value in enumerate(indices[ind+1:]):
          if dex_value == ind:
            # we've found an equation where the leading term matches the one
            # we are trying to eliminate. We should add N*the current equation
            # to this one to eliminate the leading variable. where N is the LCM
            parent_normal_component = system.planes[ind].normal_vector.coordinates[ind]
            eq_to_eliminate_normal_component = system.planes[ind+dex+1].normal_vector.coordinates[ind]
            multiple = Decimal(-(eq_to_eliminate_normal_component / parent_normal_component))

            system.add_multiple_times_row_to_row(multiple, ind, ind+dex+1)

        indices = system.indices_of_first_nonzero_terms_in_each_row()

      return system

    def compute_rref(self):
      """
      for each variable, subtract up!
      """
      tf = self.compute_triangular_form()

      indices = tf.indices_of_first_nonzero_terms_in_each_row()
      enum_list = list(enumerate(indices))
      enum_list.reverse()
      for position_in_system, variable_position in enum_list:
        # position_in_system = which equation is it, ind_val = which variable is it
        if variable_position == -1:
          # skip dis one... we don't need to do anything with this row
          continue

        bottom_eq_component = tf.planes[position_in_system].normal_vector.coordinates[variable_position]
        #reduce to 1 if necessary
        if bottom_eq_component != 1:
          tf.planes[position_in_system] = tf.planes[position_in_system] * (1 / bottom_eq_component)
          bottom_eq_component = 1

        # examine all equations above the current equation, to see if it
        # contains a variable at the ind_val index. if it does, eliminate it!
        for j in indices[:position_in_system]:
          eq_to_eliminate_in_component = tf.planes[j].normal_vector.coordinates[variable_position]
          if eq_to_eliminate_in_component != 0:
            multiple = -(eq_to_eliminate_in_component / bottom_eq_component)
            tf.add_multiple_times_row_to_row(multiple, position_in_system, j)

      return tf

    def solve_system(self):
      r = self.compute_rref()
      indices = r.indices_of_first_nonzero_terms_in_each_row()
      solution = [None] * r.dimension
      for ind, val in enumerate(indices):
        if val == -1: # this indicates there are no variables on left side of eq (no normal vector)
          if r.planes[ind].constant_term != 0:
            # this is a 0 = N case. Inconsistent
            return "System is Inconsistent"
        else:
          solution[val] = r.planes[ind].constant_term
      if any(item == None for item in solution):
        #this means that the solution is parametrized
        return "Solution has infinitely many solutions"

      return solution





    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
