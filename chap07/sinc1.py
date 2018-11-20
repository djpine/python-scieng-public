import numpy as np
def sinc(x):
    if x == 0.0:
        y = 1.0
    else:
        y = np.sin(x)/x
    return y

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-03-12

Naive sinc function that works for single
variables but not for NumPy arrays
"""
