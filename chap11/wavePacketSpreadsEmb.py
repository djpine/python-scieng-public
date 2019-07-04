import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def ww(x, t, k0, a0, vp, vg):
    tc = a0 * a0 + 1j * (0.5 * vg / k0) * t
    u = np.exp(1.0j * k0 * (x - vp * t) - 0.25 * (x - vg * t) ** 2 / tc)
    return np.real(u / np.sqrt(tc))


wavelength = 1.0
a0 = 1.0
k0 = 2 * np.pi / wavelength
vp, vg = 5.0, 10.0
period = wavelength / vp
runtime = 40 * period  # total time to follow wave
rundistance = 0.6 * vg * runtime  # total distance to plot wave
dt = period / 6.0  # time between frames
tsteps = int(runtime / dt)  # total number of times wave
# form is calculated
print('Frame time interval = {0:0.3g} ms'.format(1000 * dt))
print('Frame rate = {0:0.3g} frames/s'.format(1.0 / dt))

fig, ax = plt.subplots(figsize=(12, 3))
fig.subplots_adjust(bottom=0.2)  # allow room for axis label
x = np.arange(-5 * a0, rundistance, wavelength / 20.0)
line, = ax.plot(x, np.ma.array(x, mask=True), color='C0')
timeText = ax.text(0.9, 0.98, '', ha="left", va="top",
                   transform=ax.transAxes)
timeString = "time = {0:0.2f}"
ax.text(0.9, 0.91, r'$v_p = {0:0.1f}$'.format(vp),
        ha="left", va="top", transform=ax.transAxes)
ax.text(0.9, 0.84, r'$v_g = {0:0.1f}$'.format(vg),
        ha="left", va="top", transform=ax.transAxes)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x,t)$')
ax.set_xlim(-5 * a0, rundistance)
ax.set_ylim(-1.05, 1.05)


def animate(i):
    t = float(i) * dt
    line.set_ydata(ww(x, t, k0, a0, vp, vg))  # update y-data
    timeText.set_text(timeString.format(t))
    return line, timeText


ani = anim.FuncAnimation(fig, func=animate,
                         frames=range(tsteps),
                         interval=1000 * dt, blit=True)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani.save('wavepacketEmb.mp4', writer='ffmpeg')
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-19

Demonstrates the animation of a function with annotation
using matplotlib's FuncAnimation routine.
"""
