import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def f(x, y):
    return np.sin(x) + np.cos(y)


x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 120).reshape(-1, 1)

fig, ax = plt.subplots(figsize=(3.5, 3.5))
fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
ax.axis('off')
ims = []
for i in range(120):
    x += np.pi / 20.
    y += np.pi / 20.
    im = ax.imshow(f(x, y), cmap=plt.get_cmap('plasma'),
                   animated=True)
    ims.append([im])

ani = anim.ArtistAnimation(fig, artists=ims, interval=10,
                           repeat_delay=0)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani.save('sncs2d.mp4', writer='ffmpeg')  # need ffmpeg !)

plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-19

Makes a movie from images generated on the fly using
matplotlib's ArtistAnimation routine.  Adapted from
https://matplotlib.org/examples/animation/dynamic_image2.html
"""
