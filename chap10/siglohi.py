def siglohi(x, x0=0, n=2):
    xplus = x[x > x0] - x0
    xminus = x0 - x[x < x0]
    sigplus = ((xplus ** n).mean()) ** (1 / n)
    sigminus = ((xminus ** n).mean()) ** (1 / n)
    return sigminus, sigplus


"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-19

Function calculating the one-sided widths of a
data distribution.
"""
