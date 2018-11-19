import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def v(u, a, x, z):
    """Return the velocity vector field v = (vx, vy)
    around sphere at r=0."""
    r = np.sqrt(x*x+z*z)
    R = a/r
    RR = R*R
    cs, sn = z/r, x/r
    vr = u * cs * (1.0 - 0.5 * R * (3.0 - RR))
    vtheta = -u * sn * (1.0 - 0.25 * R * (3.0 + RR))
    vx = vr * sn + vtheta * cs
    vz = vr * cs - vtheta * sn
    return vx, vz


# Grid of x, y points
xlim, zlim = 12, 12
nx, nz = 100, 100
x = np.linspace(-xlim, xlim, nx)
z = np.linspace(-zlim, zlim, nz)
X, Z = np.meshgrid(x, z)

# Set particle radius and velocity
a, u = 1.0, 1.0

# Velocity field vector, V=(Vx, Vz) as separate components
Vx, Vz = v(u, a, X, Z)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))

# Plot the streamlines using colormap and arrow style
color = np.log(np.sqrt(Vx*Vx + Vz*Vz))
seedx = np.linspace(-xlim, xlim, 18)  # Seed streamlines evenly
seedz = -zlim * np.ones(len(seedx))   # far from particle
seed = np.array([seedx, seedz])
ax1.streamplot(x, z, Vx, Vz, color=color, linewidth=1,
               cmap='afmhot', density=5, arrowstyle='-|>',
               arrowsize=1.0, minlength=0.4, start_points=seed.T)
ax2.streamplot(x, z, Vx, Vz-u, color=color, linewidth=1,
               cmap='afmhot', density=5, arrowstyle='-|>',
               arrowsize=1.0, minlength=0.4, start_points=seed.T)
for ax in (ax1, ax2):
    # Add filled circle for sphere
    ax.add_patch(Circle((0, 0), a, color='C0', zorder=2))
    ax.set_xlabel('$x$')
    ax.set_ylabel('$z$')
    ax.set_aspect('equal')
    ax.set_xlim(-0.7*xlim, 0.7*xlim)
    ax.set_ylim(-0.7*zlim, 0.7*zlim)
fig.tight_layout()
fig.savefig('./figures/stokesFlowStream.pdf')
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-15

Streamplot example using matplotlib
"""
