import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.gridspec as gridspec


def move(L, N, eps):               # generator for updating
    x = np.sort(L*np.random.rand(N))  # speeds up algorithm
    t = 0
    moves = 1
    while moves > 0:
        changes = np.zeros(N, dtype="int")
        xc = np.copy(x)
        for i in range(N-1):
            j = i + 1
            while x[j]-x[i] < 1.0:
                rr = 2.0*(np.random.rand(2)-0.5)
                xc[i] += eps*rr[0]
                xc[j] += eps*rr[1]
                changes[i] = 1
                changes[j] = 1
                if j < N-1:
                    j += 1
                else:
                    break    # terminates while loop when j=N-1
            if x[i] < 1.0:   # periodic boundary conditions
                k = -1
                while x[i] + L - x[k] < 1.0:
                    rr = 2.0*(np.random.rand(2)-0.5)
                    xc[i] += eps*rr[0]
                    xc[k] += eps*rr[1]
                    changes[i] = 1
                    changes[k] = 1
                    k -= 1
        x = np.sort(xc % L)  # sort data for algorithm to work
        moves = np.sum(changes)
        t += 1
        yield t, moves, x, changes


N, L, eps = 80, 100, 0.25  # inputs for algorithm

circumference = float(L)
radius = circumference/(2.0*np.pi)
R = radius*np.ones(N)

fig, ax = plt.subplots(figsize=(8, 8),
                       subplot_kw=dict(polar=True))
pStill, = ax.plot(np.ma.array(R, mask=True), R,
                  'o', ms=12, color='C0')
pActiv, = ax.plot(np.ma.array(R, mask=True), R,
                  'o', ms=12, color='C1')
ax.set_rmax(1.1*radius)
ax.axis('off')

gs = gridspec.GridSpec(3, 3, width_ratios=[1, 4, 1],
                       height_ratios=[1, 2, 1])
ax2 = fig.add_subplot(gs[4], xlim=(0, 250), ylim=(0, L))
ax2.set_xlabel('time')
ax2.set_ylabel('active particles')
activity, = ax2.plot([], [], '-', color='C1')
tm, number_active = [], []


def updatePlot(mv):
    t, moves, x, changes = mv
    tm.append(t)
    number_active.append(moves)
    tmin, tmax = ax2.get_xlim()
    if t > tmax:
        ax2.set_xlim(0, 2*tmax)
    angle = 2.0*np.pi*x/L
    active = np.ma.masked_where(changes != 1, angle)
    inactive = np.ma.masked_where(changes == 1, angle)
    pStill.set_xdata(inactive)
    pActiv.set_xdata(active)
    activity.set_data(tm, number_active)
    return pStill, pActiv, activity


ani = anim.FuncAnimation(fig=fig, func=updatePlot,
                         frames=move(L, N, eps),
                         interval=10, blit=True,
                         repeat=False)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani.save('randOrgLily.mp4', writer='ffmpeg', dpi=200)
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Last edited: 2018-10-15

Demonstrates how to make an animation that continues to
execute until some condition is met.  Useful for random
processes where exact number of steps is not known ahead
of time.

To make a movie of the first 100 frames, include this line
the FuncAnimation call (needs ffmped):
ani.save('randOrgLily.mp4', writer='ffmpeg', dpi=200.
For movies with more than 2000 frames, use the keyword
argument "save_count=2000".
"""
