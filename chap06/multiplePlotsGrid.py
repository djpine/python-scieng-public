import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 200)
sin, cos, tan = np.sin(x), np.cos(x), np.tan(x)
csc, sec, cot = 1.0/sin, 1.0/cos, 1.0/tan

plt.close('all')  # Closes all open figure windows
fig, ax = plt.subplots(2, 3, figsize=(9.5, 6),
                       sharex=True, sharey=True)
ax[0, 0].plot(x, sin, color='red')
ax[0, 1].plot(x, cos, color='orange')
ax[0, 2].plot(x, np.ma.masked_where(np.abs(tan) > 20., tan),
              color='yellow')
ax[1, 0].plot(x, np.ma.masked_where(np.abs(csc) > 20., csc),
              color='green')
ax[1, 1].plot(x, np.ma.masked_where(np.abs(sec) > 20., sec),
              color='blue')
ax[1, 2].plot(x, np.ma.masked_where(np.abs(cot) > 20., cot),
              color='violet')
ax[0, 0].set_ylim(-5, 5)
ax[0, 0].set_xlim(-2*np.pi, 2*np.pi)
ax[0, 0].set_xticks(np.pi*np.array([-2, -1, 0, 1, 2]))
ax[0, 0].set_xticklabels([r'-2$\pi$', r'-$\pi$', '0',
                          r'$\pi$', r'2$\pi$'])

ax[0, 2].patch.set_facecolor('lightgray')

ylab = [['sin', 'cos', 'tan'], ['csc', 'sec', 'cot']]
for i in range(2):
    for j in range(3):
        ax[i, j].axhline(color='gray', zorder=-1)
        ax[i, j].set_ylabel(ylab[i][j])

fig.show()
fig.savefig('figures/multiplePlotsGrid.pdf')
fig.canvas.manager.window.raise_()  # fig to front

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-10

Multiple plots with matplotlib
"""
