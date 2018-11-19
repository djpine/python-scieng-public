import numpy as np
import matplotlib.pyplot as plt


def f0(t, omega, gamma, tau):
    wt = omega*t
    f1 = np.sin(wt) + (np.cos(wt)-1.0)/wt
    f2 = 1.0+(gamma/omega)*f1
    return np.exp(-t*f2/tau)


omega = 12.0
gamma = 8.0
tau = 1.0
t = np.linspace(0.01, 10.0, 500)
f = f0(t, omega, gamma, tau)

plt.rc('mathtext', fontset='stix')  # Use with mathtext
# plt.rc('text', usetex=True)        # Use with Latex
# plt.rc('font', family='serif')     # Use with Latex

fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.plot(t, f, color='C0')
ax.set_ylabel(r'$f_0(t)$', fontsize=14)
ax.set_xlabel(r'$t/\tau\quad\rm(ms)}$', fontsize=14)
ax.text(0.45, 0.95,
        r'$\Gamma(z)=\int_0^\infty x^{z-1}e^{-x}dx$',
        fontsize=16, ha='right', va='top',
        transform=ax.transAxes)
ax.text(0.45, 0.75,
        r'$e^x=\sum_{n=0}^\infty\frac{x^n}{n!}$',
        fontsize=16, ha='right', va='top',
        transform=ax.transAxes)
ax.text(0.45, 0.55,
        r'$\zeta(z)=\prod_{k=0}^\infty \frac{1}{1-p_k^{-z}}$',
        fontsize=16, ha='left', va='top',
        transform=ax.transAxes)
ax.text(0.95, 0.80,
        r'$\omega={0:0.1f},\;\gamma={1:0.1f},\;\tau={2:0.1f}$'
        .format(omega, gamma, tau),
        fontsize=14, ha='right', va='top',
        transform=ax.transAxes)
ax.text(0.85, 0.35,
        r'$e=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n$',
        fontsize=14, ha='right', va='top',
        transform=ax.transAxes)

fig.tight_layout()
fig.savefig('./figures/mplLatexDemo.pdf')
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-15

Demonstration of Latex equations in matplotlib
"""
