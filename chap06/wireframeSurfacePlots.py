import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def pmgauss(x, y):
    r1 = (x - 1) ** 2 + (y - 2) ** 2
    r2 = (x - 3) ** 2 + (y - 1) ** 2
    return 2 * np.exp(-0.5 * r1) - 3 * np.exp(-2 * r2)


a, b = 4, 3

x = np.linspace(0, a, 60)
y = np.linspace(0, b, 45)

X, Y = np.meshgrid(x, y)
Z = pmgauss(X, Y)

fig, ax = plt.subplots(1, 2, figsize=(9.2, 4),
                       subplot_kw={'projection': '3d'})
for i in range(2):
    ax[i].set_zlim(-3, 2)
    ax[i].xaxis.set_ticks(range(a + 1))  # manually set ticks
    ax[i].yaxis.set_ticks(range(b + 1))
    ax[i].set_xlabel(r'$x$')
    ax[i].set_ylabel(r'$y$')
    ax[i].set_zlabel(r'$f(x,y)$')
    ax[i].view_init(40, -30)

# Plot wireframe and surface plots.
fig.subplots_adjust(left=0.04, bottom=0.04, right=0.96,
                    top=0.96, wspace=0.05)
p0 = ax[0].plot_wireframe(X, Y, Z, rcount=40, ccount=40,
                          color='C1')
p1 = ax[1].plot_surface(X, Y, Z, rcount=50, ccount=50,
                        color='C1')
fig.subplots_adjust(left=0.0)
fig.savefig('./figures/wireframeSurfacePlots.pdf')
plt.show()
