import numpy as np
import time

a = np.linspace(0, 32, 10000000)
print(a)
startTime = time.process_time()
for i in range(len(a)):
    a[i] = a[i] * a[i]
endTime = time.process_time()
print(a)
print('Run time = {} seconds'.format(endTime - startTime))

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-20

Scripting example with formatted print output
"""
