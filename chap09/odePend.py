import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(y, t, params):
    theta, omega = y      # unpack current values
    Q, d, Omega = params  # unpack parameters
    derivs = [omega,      # list of dy/dt=f functions
              -omega/Q+np.sin(theta)+d*np.cos(Omega*t)]
    return derivs


# Parameters
Q = 2.0          # quality factor (inverse damping)
d = 1.5          # forcing amplitude
Omega = 0.65     # drive frequency

# Initial values
theta0 = 0.0     # initial angular displacement
omega0 = 0.0     # initial angular velocity

# Bundle parameters for ODE solver
params = [Q, d, Omega]

# Bundle initial conditions for ODE solver
y0 = [theta0, omega0]

# Make time array for solution
tStop = 200.
tInc = 0.05
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, y0, t, args=(params,))

# Plot results
fig = plt.figure(figsize=(9.5, 6.5))

# Plot theta as a function of time
ax1 = fig.add_subplot(221)
ax1.plot(t, psoln[:, 0], color='black')
ax1.set_xlabel('time')
ax1.set_ylabel(r'$\theta$', fontsize=14)

# Plot omega as a function of time
ax2 = fig.add_subplot(223)
ax2.plot(t, psoln[:, 1], color='black')
ax2.set_xlabel('time', fontsize=14)
ax2.set_ylabel(r'$\omega$', fontsize=14)

# Plot omega vs theta
ax3 = fig.add_subplot(122)
twopi = 2.0*np.pi
ax3.plot(psoln[:, 0] % twopi, psoln[:, 1],
         dashes=(1, 2), ms=1, color='black')
ax3.set_xlabel(r'$\theta$', fontsize=14)
ax3.set_ylabel(r'$\omega$', fontsize=14)
ax3.set_xlim(0., twopi)

plt.tight_layout()
plt.savefig('figures/odePend.pdf')
plt.show()
