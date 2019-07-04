def sinc(x):
    y = []  # empty list to store results
    for xx in x:  # loops over in x array
        if xx == 0.0:  # appends result of 1.0 to
            y += [1.0]  # y list if xx is zero
        else:  # appends result of sin(xx)/xx to y
            y += [np.sin(xx) / xx]  # list if xx is not zero
    return np.array(y)  # converts y to array and

    # returns array


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 255)
y = sinc(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y)
ax.set_xlim(-10, 10)
ax.axhline(color="gray", zorder=-1)
ax.axvline(color="gray", zorder=-1)
fig.savefig("sinc2.pdf")
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-18

sinc function written to process NumPy array
inputs with loops.  Execution is slow.
"""
