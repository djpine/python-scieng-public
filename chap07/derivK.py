def deriv(f, x, h=1.e-9, **params):
    return (f(x + h, **params) - f(x - h, **params))/(2.*h)

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-18

Calculate derivative of function f with parameters
contained in a dictionary
"""
