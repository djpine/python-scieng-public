import numpy as np
def circle(r, x0=0.0, y0=0.0, n=12):
    theta = np.linspace(0., 2*np.pi, n, endpoint=False)
    x, y  = r * np.cos(theta), r * np.sin(theta)
    return x0+x, y0+y
