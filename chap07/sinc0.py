import numpy as np


def sinc(x):
    y = np.sin(x) / x
    return y


"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2017-03-17

Naive sinc function. Fails at x=0.
"""
