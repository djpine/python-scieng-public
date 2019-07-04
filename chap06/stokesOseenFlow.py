import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Circle
from matplotlib.colors import LogNorm

matplotlib.rcParams.update({'font.size': 12})


def v(u, a, x, z, Re):
    """Return the velocity vector field v = (vx, vy)
    around sphere at r=0."""
    theta = np.arctan2(-x, -z)
    cs, sn = np.cos(theta), np.sin(theta)
    R = a / np.sqrt(x * x + z * z)
    if Re > 0:  # Oseen solution
        ex = np.exp(-0.5 * Re * (1.0 + cs) / R)
        vr = 0.5 * u * R * \
             (1.5 * (1.0 - cs) * ex - R * (3.0 * (1 - ex) / Re - R * cs))
        vtheta = 0.25 * u * R * sn * (3.0 * ex - R * R)
    else:  # Stokes solution
        RR = R * R
        vr = 0.5 * u * cs * R * (RR - 3.0)
        vtheta = 0.25 * u * sn * R * (RR + 3.0)
    vx = vr * sn + vtheta * cs
    vz = vr * cs - vtheta * sn
    return vx, vz


def stokesWake(x, Re):
    """Return parabola r[1+cos(theta)]=xi of Stokes wake"""
    z = -0.5 * (1.0 / Re - x * x * Re)
    return np.ma.masked_where(x * x + z * z < 1.0 / Re ** 2, z)


# Set particle radius and velocity
a, u = 1.0, 1.0  # normalizes radius & velocity
Re = 0.3  # Reynolds number (depends on viscosity)

# Grid of x, z points
xlim, zlim = 60, 60
nx, nz = 200, 200
x = np.linspace(-xlim, xlim, nx)
z = np.linspace(-zlim, zlim, nz)
X, Z = np.meshgrid(x, z)

# Velocity field vector, v=(Vx, Vz) as separate components
Vx, Vz = v(u, a, X, Z, Re)
R = np.sqrt(X * X + Z * Z)
speed = np.sqrt(Vx * Vx + Vz * Vz)
speed[R < a] = u  # set particle speed to u

fig, ax = plt.subplots(figsize=(8, 8))

# Plot the streamlines with an bwr colormap and arrow style
ax.streamplot(x, z, Vx, Vz, linewidth=1, density=[1, 2],
              arrowstyle='-|>', arrowsize=0.7, color='C0')
cntr = ax.pcolor(X, Z, speed,
                 norm=LogNorm(vmin=speed.min(), vmax=1),
                 cmap=plt.cm.bwr)
if Re > 0:
    ax.add_patch(Circle((0, 0), 1 / Re, color='black',
                        fill=False, ls='dashed', zorder=2))
    ax.plot(x, stokesWake(x, Re), color='black', lw=1,
            ls='dashed', zorder=2)
cbar = fig.colorbar(cntr, ax=ax, aspect=50, fraction=0.02,
                    shrink=0.9, pad=0.01)
cbar.set_label(label='fluid speed', fontsize=10)
plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize=10)
cbar.mappable.set_clim(speed.min(), 1)
cbar.draw_all()

# Add filled circle for sphere
ax.add_patch(Circle((0, 0), a, color='black', zorder=2))
ax.set_xlabel('$x/a$')
ax.set_ylabel('$z/a$')
ax.set_aspect(1)
ax.set_xlim(-xlim, xlim)
ax.set_ylim(-zlim, zlim)
ax.text(0.5, 0.99, r"$Re = {0:g}$".format(Re), ha='center',
        va='top', transform=ax.transAxes)
fig.savefig('./figures/stokesOseenFlow.pdf')
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-15

Streamplot with color example using matplotlib
"""
