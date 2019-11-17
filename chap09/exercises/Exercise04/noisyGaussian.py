from numpy.fft import fft, fftshift, ifft
import numpy as np
import matplotlib.pyplot as plt


def gaussNoisy(x, noiseAmp):
    noise = noiseAmp * (np.random.randn(len(x)))
    return np.exp(-0.5 * x * x) * (1.0 + noise)


N = 256
x = np.linspace(-4.0, 4.0, N)
y = gaussNoisy(x, 0.1)

yFT = fft(y)         # DFT in usual order with + frequencies first
YFT = fftshift(yFT)  # DFT reordered so that - frequencies are first

# Zero high frequency components of DFT
N_cuttoff = 4
yFT[N_cuttoff:N - N_cuttoff] = 0.0 + 0.0j

yFTFT = ifft(yFT)  # iDFT of cleaned up DFT

fig = plt.figure(1, frameon=False, figsize=(8, 10))

ax1 = fig.add_subplot(511)
ax1.plot(x, y, color='C0')  # Noisy Gaussian function
ax1.set_yticks((0, 0.5, 1))
ax1.set_ylim(0, 1.3)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$f\,(x)$')
ax1.axvline(color='black', lw=0.5, zorder=-1)
ax1.text(0.02, 0.95, 'noisy Gaussian', va='top',
         transform=ax1.transAxes)

ax2 = fig.add_subplot(512)
ax2.plot(YFT.real, color='C1', lw=0.5)  # Real part of DFT
ax2.set_yticks((-50, 0, 50, 100))
ax2.set_xticks((N / 4, N / 2, 3 * N / 4, N))
ax2.set_xlim(0, N)
ax2.set_xlabel('$l$')
ax2.set_ylabel('$F_l$')
ax2.axvline(x=N / 2, color='black', lw=0.5, zorder=-1)
ax2.text(0.02, 0.95, 'FFT', va='top',
         transform=ax2.transAxes)

ax3 = fig.add_subplot(513)
ax3.plot(YFT.real, color='C1', alpha=0.7, lw=0.5)  # Real part of DFT
ax3.set_yticks((-2, 0, 2))
ax3.set_xticks((N / 4, N / 2, 3 * N / 4, N))
ax3.set_xlim(0, N)
ax3.set_ylim(-2, 2)
ax3.set_xlabel('$l$')
ax3.set_ylabel('$F_l$')
ax3.axvline(x=N / 2, color='black', lw=0.5, zorder=-1)
ax3.text(0.02, 0.95, 'FFT: zoomed-in $y$-axis', va='top',
         transform=ax3.transAxes)

ax4 = fig.add_subplot(514)
ax4.plot(fftshift(yFT).real, color='C1', lw=0.5)  # Real part of DFT
ax4.set_yticks((-2, 0, 2))
ax4.set_xticks((N / 4, N / 2, 3 * N / 4, N))
ax4.set_xlim(0, N)
ax4.set_ylim(-2, 2)
ax4.set_xlabel('$l$')
ax4.set_ylabel('$F_l$')
ax4.axvline(x=N / 2, color='black', lw=0.5, zorder=-1)
ax4.text(0.02, 0.95, 'FFT: zeroed above {0:d}'.format(N_cuttoff),
         va='top', transform=ax4.transAxes)

ax5 = fig.add_subplot(515)
ax5.plot(x, yFTFT, color='C0')  # Inverse of cleaned up DFT
ax5.plot(x, y, color='gray', lw=0.5)
ax5.set_yticks((0, 0.5, 1))
ax5.set_ylim(0, 1.3)
ax5.set_xlabel('$x$')
ax5.set_ylabel('$f\,(x)$')
ax5.axvline(color='gray', lw=0.5, zorder=-1)
ax5.axvline(color='black', lw=0.5, zorder=-1)
ax5.text(0.02, 0.95, 'retransformed filtered signal & original',
         va='top', transform=ax5.transAxes)

plt.tight_layout()
plt.savefig('FAnoisyGauss.pdf')
plt.show()
