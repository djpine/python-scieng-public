""" Demonstrates the following:
      ~ multiple plots in a single figure
      ~ plotting logarithmic axes
      ~ user-defined functions
      ~ ''where'' function, NumPy array conditional"""

import numpy as np
import matplotlib.pyplot as plt


# Define the sinc function, with output for x=0
# defined as a special case to avoid division by zero
def s(x):
    a = np.where(x == 0., 1., np.sin(x) / x)
    return a


x = np.arange(0., 10., 0.1)
y = np.exp(x)

t = np.linspace(-15., 15., 150)
z = s(t)

# create a figure window
fig = plt.figure(figsize=(9, 7))

# subplot: linear plot of exponential
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, y, 'C0')
ax1.set_xlabel('time (ms)')
ax1.set_ylabel('distance (mm)')
ax1.set_title('exponential')

# subplot: semi-log plot of exponential
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, y, 'C2')
ax2.set_yscale('log')
# ax2.semilogy(x, y, 'C2')  # same as 2 previous lines
ax2.set_xlabel('time (ms)')
ax2.set_ylabel('distance (mm)')
ax2.set_title('exponential')

# subplot: wide subplot of sinc function
ax3 = fig.add_subplot(2, 1, 2)
ax3.plot(t, z, 'C3')
ax3.axhline(color='gray')
ax3.axvline(color='gray')
ax3.set_xlabel('angle (deg)')
ax3.set_ylabel('electric field')
ax3.set_title('sinc function')

# fig.tight_layout() adjusts white space to
# avoid collisions between subplots
fig.tight_layout()
fig.savefig("figures/multiplePlots1window.pdf")
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-22

Multiple plots in a window with matplotlib
"""
