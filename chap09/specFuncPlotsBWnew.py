import numpy as np
import numpy.polynomial
import scipy.special
import matplotlib.pyplot as plt

# create a figure window with subplots
fig, ax = plt.subplots(3, 2, figsize=(9.3, 6.5))

# create arrays for a few Bessel functions and plot them
x = np.linspace(0, 20, 256)
j0 = scipy.special.jv(0, x)  # see also j0(x)
j1 = scipy.special.jv(1, x)  # see also j1(x)
y0 = scipy.special.yv(0, x)  # see also y0(x)
y1 = scipy.special.yv(1, x)  # see also y1(x)
ax[0, 0].plot(x, j0, color='black')
ax[0, 0].plot(x, j1, color='black', dashes=(5, 2))
ax[0, 0].plot(x, y0, color='black', dashes=(3, 2))
ax[0, 0].plot(x, y1, color='black', dashes=(1, 2))
ax[0, 0].axhline(color="grey", ls="--", zorder=-1)
ax[0, 0].set_ylim(-1, 1)
ax[0, 0].text(0.5, 0.95, 'Bessel', ha='center',
              va='top', transform=ax[0, 0].transAxes)

# gamma function
x = np.linspace(-3.5, 6., 3601)
g = scipy.special.gamma(x)
g = np.ma.masked_outside(g, -100, 400)
ax[0, 1].plot(x, g, color='black')
ax[0, 1].set_xlim(-3.5, 6)
ax[0, 1].axhline(color="grey", ls="--", zorder=-1)
ax[0, 1].axvline(color="grey", ls="--", zorder=-1)
ax[0, 1].set_ylim(-20, 100)
ax[0, 1].text(0.5, 0.95, 'Gamma', ha='center',
              va='top', transform=ax[0, 1].transAxes)

# error function
x = np.linspace(0, 2.5, 256)
ef = scipy.special.erf(x)
ax[1, 0].plot(x, ef, color='black')
ax[1, 0].set_ylim(0, 1.1)
ax[1, 0].text(0.5, 0.95, 'Error', ha='center',
              va='top', transform=ax[1, 0].transAxes)

# Airy function
x = np.linspace(-15, 4, 256)
ai, aip, bi, bip = scipy.special.airy(x)
ax[1, 1].plot(x, ai, color='black')
ax[1, 1].plot(x, bi, color='black', dashes=(5, 2))
ax[1, 1].axhline(color="grey", ls="--", zorder=-1)
ax[1, 1].axvline(color="grey", ls="--", zorder=-1)
ax[1, 1].set_xlim(-15, 4)
ax[1, 1].set_ylim(-0.5, 0.6)
ax[1, 1].text(0.5, 0.95, 'Airy', ha='center',
              va='top', transform=ax[1, 1].transAxes)

# Legendre polynomials
x = np.linspace(-1, 1, 256)
lp0 = numpy.polynomial.Legendre.basis(0)(x)
lp1 = numpy.polynomial.Legendre.basis(1)(x)
lp2 = numpy.polynomial.Legendre.basis(2)(x)
lp3 = numpy.polynomial.Legendre.basis(3)(x)
ax[2, 0].plot(x, lp0, color='black')
ax[2, 0].plot(x, lp1, color='black', dashes=(5, 2))
ax[2, 0].plot(x, lp2, color='black', dashes=(3, 2))
ax[2, 0].plot(x, lp3, color='black', dashes=(1, 2))
ax[2, 0].axhline(color="grey", ls="--", zorder=-1)
ax[2, 0].axvline(color="grey", ls="--", zorder=-1)
ax[2, 0].set_ylim(-1, 1.1)
ax[2, 0].text(0.5, 0.9, 'Legendre', ha='center',
              va='top', transform=ax[2, 0].transAxes)

# Laguerre polynomials
x = np.linspace(-5, 8, 256)
lg0 = numpy.polynomial.Laguerre.basis(0)(x)
lg1 = numpy.polynomial.Laguerre.basis(1)(x)
lg2 = numpy.polynomial.Laguerre.basis(2)(x)
lg3 = numpy.polynomial.Laguerre.basis(3)(x)
ax[2, 1].plot(x, lg0, color='black')
ax[2, 1].plot(x, lg1, color='black', dashes=(5, 2))
ax[2, 1].plot(x, lg2, color='black', dashes=(3, 2))
ax[2, 1].plot(x, lg3, color='black', dashes=(1, 2))
ax[2, 1].axhline(color="grey", ls="--", zorder=-1)
ax[2, 1].axvline(color="grey", ls="--", zorder=-1)
ax[2, 1].set_xlim(-5, 8)
ax[2, 1].set_ylim(-5, 10)
ax[2, 1].text(0.5, 0.9, 'Laguerre', ha='center',
              va='top', transform=ax[2, 1].transAxes)
plt.tight_layout()
plt.savefig("figures/specFuncPlotsBW.pdf")
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-17

Demonstrates calls to SciPy special functions and
plots them.
"""
