def lineFit(x, y):
    ''' Returns slope and y-intercept of linear fit to (x,y)
    data set'''
    xavg = x.mean()
    slope = (y * (x-xavg)).sum()/(x * (x-xavg)).sum()
    yint = y.mean() - slope*xavg
    return slope, yint


"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-18

Calculate derivative of function f with parameters
contained in a dictionary
"""
