import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(7.5, 4.5))
xa = np.linspace(0.01, 6.0, 150)
ya = np.sin(np.pi*xa)/xa
ax1.plot(xa, ya, '-C0')
ax1.set_xlabel('x (micrometers)')
# Make y-axis label, ticks and numbers match line color.
ax1.set_ylabel('oscillate', color='C0')
ax1.tick_params('y', colors='C0')

ax2 = ax1.twinx()  # use same x-axis for a 2nd (right) y-axis
xb = np.arange(0.3, 6.0, 0.3)
yb = np.exp(-xb*xb/9.0)
ax2.plot(xb, yb, 'oC3')
ax2.set_ylabel('decay', color='C3')  # axis label
ax2.tick_params('y', colors='C3')    # ticks & numbers

fig.tight_layout()
plt.show()
plt.savefig('figures/twoAxes.pdf')
