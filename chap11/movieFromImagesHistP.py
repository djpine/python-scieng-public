import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import pandas as pd
from glob import glob
from PIL import Image


def angle(x, y):
    a = np.array([x[0]-x[1], y[0]-y[1]])
    b = np.array([x[2]-x[1], y[2]-y[1]])
    cs = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    if cs > 1.0:
        cs = 1.0
    elif cs < -1.0:
        cs = -1.0
    return np.rad2deg(np.arccos(cs))


r = pd.read_excel('trajectories.xlsx')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))
ax1.axis('off')

ims = []
angles = []
for i, fname in enumerate(sorted(glob('pngs/s0*.png'))):
    # print(fname)  # uncomment to follow loading of image frames
    im = ax1.imshow(Image.open(fname), animated=True)  # image
    x = np.array([r['x1'][i], r['xc'][i], r['x2'][i]])  # 3 balls
    y = np.array([r['y1'][i], r['yc'][i], r['y2'][i]])  # joined by
    ima, = ax1.plot(x, y, 'o-', color=[1, 1, 0.7])      # 2 lines
    theta = angle(x, y)
    angles.append(theta)
    imb = ax1.text(0.05, 0.95, 'frame = {0:d}\nangle = {1:0.0f}°'
                   .format(i, theta), va='top', ha='left',
                   color=[1, 1, 0.7], transform=ax1.transAxes)
    a, b = np.histogram(angles, bins=15, range=(90, 180),
                        density=True)  # normed=True is depricated
    xx = 0.5*(b[:-1]+b[1:])
    ax2.set_ylim(0, 0.03)
    ax2.set_xlabel('angle (degrees)')
    im2, = ax2.plot(xx, a, '-oC0')
    ims.append([im, ima, imb, im2])
    # plot histogram
    # im2 = ax2.bar(xx, a, width=0.9*(b[1]-b[0]), color='C0')
    # ims.append([im, ima, imb] + list(im2))
    plt.tight_layout()

ani = anim.ArtistAnimation(fig, artists=ims, interval=33,
                           repeat=False, blit=False)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani.save('movieFromImagesHistP.mp4', writer='ffmpeg')
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Last edited: 2018-09-15

Demonstrates how to make an animation that combines a
sequence of frames with a data plot.
"""
