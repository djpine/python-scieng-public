from numpy.fft import fft, fftshift, ifft
import numpy as np
import matplotlib.pyplot as plt


def gaussNoisy(x, noiseAmp):
    noise = noiseAmp*(np.random.randn(len(x)))
    return np.exp(-x*x/2.0) * (1.0+noise)


N = 256
x = np.linspace(-4.0, 4.0, N)
y = gaussNoisy(x, 0.1)

yFT = fft(y)         # DFT in usual order with + frequencies first
YFT = fftshift(yFT)  # DFT reordered so that - frequencies are first

# Zero high frequency components of DFT
N_cuttoff = 4
yFT[N_cuttoff:N-N_cuttoff] = 0.0+0.0j

yFTFT = ifft(yFT)       # iDFT of cleaned up DFT

fig = plt.figure(1, frameon=False, figsize=(8, 3))

ax1 = fig.add_subplot(111)
ax1.plot(x, y, color='gray', lw=0.5, label='original')
ax1.plot(x, yFTFT, color='C0', label='retransformed filtered signal')
ax1.set_yticks((0, 0.5, 1))
ax1.set_ylim(0, 1.3)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$f\,(x)$')
ax1.axvline(color='gray', lw=0.5, zorder=-1)
ax1.axvline(color='black', lw=0.5, zorder=-1)
ax1.legend()

plt.tight_layout()

plt.savefig('../figures/FAnoisyGaussInBook.pdf')

plt.show()
