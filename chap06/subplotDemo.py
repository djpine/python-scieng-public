import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 8., 0.04)
y = np.sqrt((8. / theta) ** 2 - 1.)
ytan = np.tan(theta)
ytan = np.ma.masked_where(np.abs(ytan) > 20., ytan)
ycot = 1. / np.tan(theta)
ycot = np.ma.masked_where(np.abs(ycot) > 20., ycot)

plt.figure(figsize=(8.5, 6))

plt.subplot(2, 1, 1)
plt.plot(theta, y, linestyle=':')
plt.plot(theta, ytan)
plt.xlim(0, 8)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)
plt.axvline(x=np.pi / 2., color="gray", linestyle='--',
            zorder=-1)
plt.axvline(x=3. * np.pi / 2., color="gray", linestyle='--',
            zorder=-1)
plt.axvline(x=5. * np.pi / 2., color="gray", linestyle='--',
            zorder=-1)
plt.xlabel("theta")
plt.ylabel("tan(theta)")

plt.subplot(2, 1, 2)
plt.plot(theta, -y, linestyle=':')
plt.plot(theta, ycot)
plt.xlim(0, 8)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)
plt.axvline(x=np.pi, color="gray", linestyle='--',
            zorder=-1)
plt.axvline(x=2. * np.pi, color="gray", linestyle='--',
            zorder=-1)
plt.xlabel("theta")
plt.ylabel("cot(theta)")

plt.savefig('figures/subplotDemo.pdf')
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-15

Subplots using pyplot in matplotlib
"""
