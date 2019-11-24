import numpy as np
import matplotlib.pyplot as plt


def gauss(x, a=1.0):
    return a * np.exp(-0.5 * x * x)


N = 10000
r = np.random.rand(N)
rn = np.random.randn(N)
x = np.linspace(-4, 4, 128)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 2.5))
ax1.hist(r, 50, color='lightgray')
ax1.text(0.05, 0.98, 'np.rand({0:d})'.format(N),
         ha='left', va='top', transform=ax1.transAxes)
ax2.hist(rn, 50, color='gray')
ax2.plot(x, gauss(x, 2 * np.pi * np.sqrt(N)))
ax2.text(0.05, 0.98, 'np.randn({0:d})'.format(N),
         ha='left', va='top', transform=ax2.transAxes)
fig.subplots_adjust(left=0.06, right=0.95)

plt.savefig('randHist.pdf')
plt.show()
