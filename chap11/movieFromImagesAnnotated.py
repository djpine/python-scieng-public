import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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


r = pd.read_excel('trajectories.xlsx', usecols='A:F')

fig, ax = plt.subplots(figsize=(3.6, 3.5))
fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
ax.axis('off')

ims = []
angles = []
for i, fname in enumerate(sorted(glob('pngs/s[0-2]*.png'))):
    # print(fname)  # uncomment to follow loading of images
    im = ax.imshow(Image.open(fname), animated=True)
    # Make 3 solid points connect by two bars
    x = np.array([r['x1'][i], r['xc'][i], r['x2'][i]])
    y = np.array([r['y1'][i], r['yc'][i], r['y2'][i]])
    ima, = ax.plot(x, y, 'o-', color=[1, 1, 0.7])
    # Get angle between bars & write on movie frames
    theta = angle(x, y)
    angles.append(theta)
    imb = ax.text(0.05, 0.95, 'frame = {0:d}\nangle = {1:0.0f}°'
                  .format(i, theta), va='top', ha='left',
                  color=[1, 1, 0.7], transform=ax.transAxes)
    ims.append([im, ima, imb])

ani = animation.ArtistAnimation(fig, artists=ims, interval=33,
                                repeat=False)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani.save('movieFromImagesAnnotated.mp4', writer='ffmpeg')
plt.show()

"""
Demonstrates how to read a sequence of images from disk,
animate them for display, overlay other Artists onto the
image, and then save the animation.

Author: David J. Pine
"""
