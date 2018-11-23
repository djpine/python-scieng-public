import numpy as np
import matplotlib.pyplot as plt


def LineFitWt(x, y, dy):
    """
    Fit to straight line.
    Inputs: x, y, and dy (y-uncertainty) arrays.
    Ouputs: slope and y-intercept of best fit to data.
    """
    dy2 = dy**2
    norm = (1./dy2).sum()
    xhat = (x/dy2).sum() / norm
    yhat = (y/dy2).sum() / norm
    slope = ((x-xhat)*y/dy2).sum()/((x-xhat)*x/dy2).sum()
    yint = yhat - slope*xhat
    dy2_slope = 1./((x-xhat)*x/dy2).sum()
    dy2_yint = dy2_slope * (x*x/dy2).sum() / norm
    return slope, yint, np.sqrt(dy2_slope), np.sqrt(dy2_yint)


def redchisq(x, y, dy, slope, yint):
    chisq = (((y-yint-slope*x)/dy)**2).sum()
    return chisq/float(x.size-2)

# Read data from data file
t, N, dN = np.loadtxt("betaDecay.txt", skiprows=2, unpack=True)

# Code to tranform & fit data starts here

# Transform data and parameters to linear form: Y = A + B*X
X = t          # transform t data for fitting (trivial)
Y = np.log(N)  # transform N data for fitting
dY = dN/N      # transform uncertainties for fitting

# Fit transformed data X, Y, dY --> fitting parameters A & B
# Also returns uncertainties in A and B
B, A, dB, dA = LineFitWt(X, Y, dY)
# Return reduced chi-squared
redchisqr = redchisq(X, Y, dY, B, A)

# Determine fitting parameters for exponential function
# N = N0 exp(-t/tau) ...
N0 = np.exp(A)
tau = -1.0/B
# ... and their uncertainties
dN0 = N0 * dA
dtau = tau**2 * dB

# Code to plot transformed data and fit starts here

# Create line corresponding to fit using fitting parameters
# Only two points are needed to specify a straight line
Xext = 0.05*(X.max()-X.min())
Xfit = np.array([X.min()-Xext, X.max()+Xext])
Yfit = A + B*Xfit

plt.errorbar(X, Y, dY, fmt="oC0")
plt.plot(Xfit, Yfit, "-C1", zorder=-1)
plt.xlim(0, 100)
plt.ylim(1.5, 7)
plt.title(r"$\mathrm{Fit\ to:}\ \ln N = -t/\tau + \ln N_0$")
plt.xlabel("$t$")
plt.ylabel("ln($N$)")
plt.text(50, 6.6, "A = ln N0 = {0:0.2f} $\pm$ {1:0.2f}"
         .format(A, dA))
plt.text(50, 6.3, "B = -1/tau = {0:0.4f} $\pm$ {1:0.4f}"
         .format(-B, dB))
plt.text(50, 6.0, "$\chi_r^2$ = {0:0.3f}"
         .format(redchisqr))
plt.text(50, 5.7, "N0 = {0:0.0f} $\pm$ {1:0.0f}"
         .format(N0, dN0))
plt.text(50, 5.4, "tau = {0:0.1f} $\pm$ {1:0.1f} days"
         .format(tau, dtau))
plt.show()
plt.savefig("betaDecay.pdf")

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-20

Uses linear regression for fitting an exponential
function by taking the logarithm of the y-data.
"""
