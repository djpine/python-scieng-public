import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

width = 2.0
freq = 0.5

t = np.linspace(-10, 10, 128)
g = np.exp(-np.abs(t)/width) * np.sin(2.0*np.pi*freq*t)
dt = t[1]-t[0]  # increment between times in time array

G = fftpack.fft(g)  # FFT of g
f = fftpack.fftfreq(g.size, d=dt)  # FFT frequenies
f = fftpack.fftshift(f)  # shift freqs from min to max
G = fftpack.fftshift(G)  # shift G order to match f

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))
ax1.plot(t, g)
ax1.set_xlabel(r'$t$')
ax1.set_ylabel(r'$g(t)$')
ax1.set_ylim(-1, 1)
ax2.plot(f, np.real(G), color='dodgerblue',
         label='real part')
ax2.plot(f, np.imag(G), color='coral',
         label='imaginary part')
ax2.legend()
ax2.set_xlabel(r'$f$')
ax2.set_ylabel(r'$G(f)$')
fig.tight_layout()
fig.savefig('figures/fftExample.pdf')
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-17

Demonstrates calls to SciPy special functions and
plots them.
"""
