# Calculates the distance between two 3d Cartesian
# coordinates
import numpy as np

x1, y1, z1 = 23.7, -9.2, -7.8
x2, y2, z2 = -3.5, 4.8, 8.1

dr = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-01-06

Second scripting example
"""
