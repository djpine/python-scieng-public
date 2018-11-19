import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm   # color maps
import matplotlib


def pmgauss(x, y):
    r1 = (x-1)**2 + (y-2)**2
    r2 = (x-3)**2 + (y-1)**2
    return 2*np.exp(-0.5*r1) - 3*np.exp(-2*r2)


a, b = 4, 3

x = np.linspace(0, a, 60)
y = np.linspace(0, b, 45)

X, Y = np.meshgrid(x, y)
Z = pmgauss(X, Y)

fig, ax = plt.subplots(2, 2, figsize=(9.4, 6.5),
                       sharex=True, sharey=True,
                       gridspec_kw={'width_ratios': [4, 5]})

CS0 = ax[0, 0].contour(X, Y, Z, 8, colors='k')
ax[0, 0].clabel(CS0, fontsize=9, fmt='%0.1f')
matplotlib.rcParams['contour.negative_linestyle'] = 'dashed'
ax[0, 0].plot(X, Y, 'o', ms=1, color='lightgray', zorder=-1)

CS1 = ax[0, 1].contourf(X, Y, Z, 12, cmap=cm.gray, zorder=0)
cbar1 = fig.colorbar(CS1, shrink=0.8, ax=ax[0, 1])
cbar1.set_label(label='height', fontsize=10)
plt.setp(cbar1.ax.yaxis.get_ticklabels(), fontsize=8)

lev2 = np.arange(-3, 2, 0.3)
CS2 = ax[1, 0].contour(X, Y, Z, levels=lev2, colors='k',
                       linewidths=0.5)
ax[1, 0].clabel(CS2, lev2[1::2], fontsize=9, fmt='%0.1f')

CS3 = ax[1, 1].contour(X, Y, Z, 10, colors='gray')
ax[1, 1].clabel(CS3, fontsize=9, fmt='%0.1f')
im = ax[1, 1].imshow(Z, interpolation='bilinear',
                     origin='lower', cmap=cm.gray,
                     extent=(0, a, 0, b))
cbar2 = fig.colorbar(im, shrink=0.8, ax=ax[1, 1])
cbar2.set_label(label='height', fontsize=10)
plt.setp(cbar2.ax.yaxis.get_ticklabels(), fontsize=8)

for i in range(2):
    ax[1, i].set_xlabel(r'$x$', fontsize=14)
    ax[i, 0].set_ylabel(r'$y$', fontsize=14)
    for j in range(2):
        ax[i, j].set_aspect('equal')
        ax[i, j].set_xlim(0, a)
        ax[i, j].set_ylim(0, b)
fig.subplots_adjust(left=0.06, bottom=0.07, right=0.99,
                    top=0.99, wspace=0.06, hspace=0.09)
fig.savefig('./figures/contour4.pdf')
fig.show()


"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-10

Contour plot examples with matplotlib
"""
