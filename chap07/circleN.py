import numpy as np


def circle(r, x0, y0, n):
    theta = np.linspace(0., 2*np.pi, n, endpoint=False)
    x, y = r * np.cos(theta), r * np.sin(theta)
    return x0+x, y0+y


"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-18

Circle plot centered at (x0, y0) with matplotlib
"""
