import numpy as np
import time
a = np.linspace(0, 32, 10000000)
print(a)
startTime = time.process_time()
a = a*a
endTime = time.process_time()
print(a)
print('Run time = {} seconds'.format(endTime-startTime))
