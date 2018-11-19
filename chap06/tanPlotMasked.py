import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 10., 0.04)
ytan = np.tan(theta)
ytanM = np.ma.masked_where(np.abs(ytan) > 20., ytan)

plt.figure(figsize=(8.5, 4.2))
plt.plot(theta, ytanM)
plt.ylim(-8, 8)  # restricts y-axis range from -8 to +8
plt.axhline(color="gray", zorder=-1)
plt.savefig('figures/tanPlotMasked.pdf')
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2017-05-27

tangent plot with masking to leave out extraneous
vertical lines where tangent diverges using matplotlib
"""
