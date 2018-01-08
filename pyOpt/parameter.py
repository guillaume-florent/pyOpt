#!/usr/bin/env python
# coding: utf-8

"""
pyOpt_parameter

Holds the Python Design Optimization Classes (base and inherited).

Copyright (c) 2008-2014 by pyOpt Developers
All rights reserved.
Revision: 1.0   $Date: 23/05/2008 21:00$


Developers:
-----------
- Dr. Ruben E. Perez (RP)

History
-------
    v. 1.0  - Initial Class Creation (RP, 2008)

"""

from __future__ import print_function

__version__ = '$Revision: $'

inf = 10.E+20  # define a value for infinity


class Parameter(object):
    """Optimization Parameter Class"""
    def __init__(self, name, value=0.0):
        """
        Parameter Class Initialization

        **Arguments:**

        - name -> STR: Parameter Name

        **Keyword arguments:**

        - value -> SCALAR: Parameter Value, *Default* = 0.0

        Documentation last updated:  Feb. 07, 2011 - Peter W. Jansen
        """
        self.name = name
        self.value = value

    def ListAttributes(self):
        """
        Print Structured Attributes List

        Documentation last updated:  May. 23, 2008 - Ruben E. Perez

        """
        ListAttributes(self)

    def __str__(self):
        """Print Structured List of Parameter

        Documentation last updated:  May. 23, 2008 - Ruben E. Perez

        """
        return ('Name    Value\n' + '	 ' +
                str(self.name).center(9) + '%14f\n' % self.value)


def ListAttributes(self):
    """Print Structured Attributes List

    Documentation last updated:  March. 24, 2008 - Ruben E. Perez

    """
    print('\n')
    print('Attributes List of: ' + repr(self.__dict__['name']) + ' - ' +
          self.__class__.__name__ + ' Instance\n')
    self_keys = self.__dict__.keys()
    self_keys.sort()
    for key in self_keys:
        if key != 'name':
            print(str(key) + ' : ' + repr(self.__dict__[key]))
    print('\n')


if __name__ == '__main__':
    print('Testing ...')

    # Test Parameter
    par = Parameter('x')
    par.ListAttributes()
