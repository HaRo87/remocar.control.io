'''
 Copyright (C) 2018 Robert Hansel
 
 This software may be modified and distributed under the terms
 of the MIT license.  See the LICENSE file for details.
'''
class ControlError(Exception):
    """
    Base class for exceptions in the remocar-control module.
    """
    pass

class ControlConfigError(ControlError):
    """
    Exception raised for errors related to the configuration
    of this module.

    Parameters
    ----------
    expr: 
        Input expression in which the error occurred.
    msg: str
        Explanation of the error.
    """
    msg = ''

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
