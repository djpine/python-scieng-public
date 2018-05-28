import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 10., 0.04)
ytan = np.tan(theta)

plt.figure(figsize=(8.5, 4.2))
plt.plot(theta, ytan)
plt.ylim(-8, 8)  # restricts range of y axis from -8 to +8
plt.axhline(color="gray", zorder=-1)
plt.show()
plt.savefig('figures/tanPlot1.pdf')
