import numpy as np

dataPt, time, height, error = np.loadtxt("MyData.txt",
                                         skiprows=5,
                                         unpack=True)

info = 'Data for falling mass experiment'
info += '\nDate: 16-Aug-2016'
info += '\nData taken by Lauren and John'
info += '\n\n data point time (sec) height (mm) '
info += 'uncertainty (mm)'

np.savetxt('ReadWriteMyDataHeader.txt',
           list(zip(dataPt, time, height, error)),
           header=info, fmt="%12.1f")
