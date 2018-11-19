import numpy as np
import matplotlib.pyplot as plt

# read data from file
xdata, ydata, yerror = np.loadtxt('expDecayData.txt',
                                  unpack=True)

# create theoretical fitting curve
x = np.linspace(0, 45, 128)
y = 1.1 + 3.0*x*np.exp(-(x/10.0)**2)

# create plot
plt.figure(1, figsize=(6, 4))
plt.plot(x, y, '-C0', label="theory")
plt.errorbar(xdata, ydata, fmt='oC1', label="data",
             xerr=0.75, yerr=yerror, ecolor='black')
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right')

# save plot to file
plt.savefig('figures/ExpDecay.pdf')

# display plot on screen
plt.show()


"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2017-05-27

Plot with error bars with matplotlib
"""
