import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(w, t, params):
    x, y, z = w             # unpack current values
    a, b, c = params        # unpack parameters
    derivs = [a * (y - x),  # list of dw/dt=f functions
              (c - a) * x - x * z + c * y,
              x * y - b * z]
    return derivs


# Parameters
a = 40.0  # quality factor (inverse damping)
b = 5.0   # forcing amplitude
c = 30.0  # drive frequency

# Initial values
x0 = -10.0  # initial angular displacement
y0 = 0.0    # initial angular velocity
z0 = 35.0

# Bundle parameters for ODE solver
params = [a, b, c]

# Bundle initial conditions for ODE solver
w0 = [x0, y0, z0]

# Make time array for solution
tStop = 10.
tInc = 0.005
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, w0, t, args=(params,))
x, y, z, = psoln[:, 0], psoln[:, 1], psoln[:, 2]

# Plot results
fig, ax = plt.subplots(3, 2, figsize=(8, 8),
                       gridspec_kw={'width_ratios': [2, 1]})

# Plot x as a function of time
ax[0, 0].plot(t, x, color='C0', lw=0.5)
ax[0, 0].set_xlabel('time')
ax[0, 0].set_ylabel('$x$')

# Plot y as a function of time
ax[1, 0].plot(t, y, color='C1', lw=0.5)
ax[1, 0].set_xlabel('time')
ax[1, 0].set_ylabel('$y$')

# Plot z as a function of time
ax[2, 0].plot(t, z, color='C2', lw=0.5)
ax[2, 0].set_xlabel('time')
ax[2, 0].set_ylabel('$z$')

# Plot y vs x
ax[0, 1].plot(y, x, '.', ms=1, color='C5')
ax[0, 1].set_xlabel('$y$')
ax[0, 1].set_ylabel('$x$')

# Plot z vs y
ax[1, 1].plot(z, y, '.', ms=1, color='C4')
ax[1, 1].set_xlabel('$z$')
ax[1, 1].set_ylabel('$y$')

# Plot x vs z
ax[2, 1].plot(x, z, '.', ms=1, color='C3')
ax[2, 1].set_xlabel('$x$')
ax[2, 1].set_ylabel('$z$')

plt.tight_layout()
plt.savefig('../figures/genesio.pdf')
plt.savefig('genesio.pdf')
plt.show()
