import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from PIL import Image, ImageEnhance
from glob import glob

framesDir = 'movieSyncFrames'  # movie frames directory
framesData = 'movieSyncData.csv'  # data file with intensities
time, uv, blue = np.loadtxt(framesData, skiprows=1, unpack=True, delimiter=',')

# Static parts of plot come first
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))
fig.subplots_adjust(bottom=0.15, top=0.95, left=0, right=0.98)
ax1.axis('off')
ax2.set_xlim([0, time.max()])
ax2.set_ylim([0.85, 1.05])
ax2.plot(time, uv + blue, dashes=(5, 2), color='gray', lw=1)
ax2.set_xlabel('time (s)')
ax2.set_ylabel('normalized integrated intensity')
ax2.set_yticks([0.85, 0.9, 0.95, 1., 1.05])
# Set up plot containers for ax2
plotdotUV, = ax2.plot(np.nan, np.nan, 'o', color='violet',
    ms=6, alpha=0.7)
plotdotBlue, = ax2.plot(np.nan, np.nan, 'o', color='blue',
    ms=6, alpha=0.7)
plotlineB, = ax2.plot(np.nan, np.nan, '-', color='blue', lw=2)
plotlineU, = ax2.plot(np.nan, np.nan, '-', color='violet', lw=2)

# Mask data you do not want to plot
uvM = np.where(uv > 0.9, uv, np.nan)
blueM = np.where(blue > 0.9, blue, np.nan)

# Dynamic parts of plot come next
ims = []
for i, fname in enumerate(sorted(glob(framesDir + '/sp*.png'))):
    # print(fname)  # uncomment to follow loading of image frames
    if uv[i] >= blue[i]:
        im = ax1.imshow(Image.open(fname), animated=True)
        textUV = ax1.text(320, 20, 'UV ON', color='white',
            weight='bold')
    else:
        img0 = Image.open(fname)
        # Increase brightness of uv-illuminated images
        img0 = ImageEnhance.Brightness(img0).enhance(2.5)
        im = ax1.imshow(img0, animated=True)
        textUV = ax1.text(320, 20, 'UV OFF', color='yellow',
            weight='bold')
    ims.append([im, textUV])


def animate(i):
    plotdotUV.set_data(time[i], uvM[i])
    plotdotBlue.set_data(time[i], blueM[i])
    plotlineB.set_data(time[0:i], blueM[0:i])
    plotlineU.set_data(time[0:i], uvM[0:i])
    return plotdotUV, plotdotBlue, plotlineB, plotlineU


ani1 = anim.ArtistAnimation(fig, artists=ims, interval=33,
    repeat=False)
ani2 = anim.FuncAnimation(fig, func=animate,
    frames=range(time.size), interval=33,
    repeat=False, blit=False,
    event_source=ani1.event_source)
# Uncomment to save as mp4 movie file.  Need ffmpeg.
# ani2.save('movieSyncPlot1.mp4', extra_anim=(ani1, ),
#           writer='ffmpeg', dpi=200)
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Last edited: 2018-09-20

Demonstrates how to combine a movie animated from images
using ArtistAnimation with a function animation made with
FuncAnimation into a single movie with frames from each
animation synchronized with each other.
"""
