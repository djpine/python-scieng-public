import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

# Read in data
bp = pd.read_excel('BloodPressure.xlsx', usecols='A:E',
                   parse_dates=[['Date', 'Time']])
bp = bp.set_index('Date_Time')
# Divide data into AM and PM sets
diaAM = bp.loc[bp.index.hour < 12, 'BP_dia']
diaPM = bp.loc[bp.index.hour >= 12, 'BP_dia']
sysAM = bp.loc[bp.index.hour < 12, 'BP_sys']
sysPM = bp.loc[bp.index.hour >= 12, 'BP_sys']
PulseAM = bp.loc[bp.index.hour < 12, 'Pulse']
PulsePM = bp.loc[bp.index.hour >= 12, 'Pulse']
# Set up figure with 2 subplots and plot BP data

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,
                               gridspec_kw={'height_ratios': [2, 1]},
                               figsize=(10, 6))
fig.subplots_adjust(left=0.065, right=0.99, hspace=0.06)
sysPM.plot(ax=ax1, marker='o', ms=3, lw=0, color='C1',
           label='systolic PM')
sysAM.plot(ax=ax1, marker='o', ms=3, lw=0, color='C1',
           mfc='white', label='systolic AM')
diaPM.plot(ax=ax1, marker='o', ms=3, lw=0, color='C0',
           label='diastolic PM')
diaAM.plot(ax=ax1, marker='o', ms=3, lw=0, color='C0',
           mfc='white', label='diastolic AM')
# Average values of blood pressures with arrows labeling them
dtlab = datetime(2017, 6, 29)
bpavgs = (sysAM.mean(), sysPM.mean(), diaAM.mean(),
          diaPM.mean())
ytext = ('bottom', 'top')
tavgs = ('AM average = {0:0.0f}'.format(bpavgs[0]),
         'PM average = {0:0.0f}'.format(bpavgs[1]),
         'AM average = {0:0.0f}'.format(bpavgs[2]),
         'PM average = {0:0.0f}'.format(bpavgs[3]))
aprops = dict(facecolor='black', width=1, headlength=5,
              headwidth=5)
for i, bpa in enumerate(bpavgs):
    ax1.annotate(tavgs[i], xy=(dtlab, bpa),
                 xytext=((15, (-1)**(i % 2)*15)),
                 textcoords='offset points',
                 arrowprops=aprops, ha='left',
                 va=ytext[i % 2])
# Lines indicating average blood pressures
ax1.axhline(y=sysPM.mean(), color='C1', lw=0.75, zorder=-1)
ax1.axhline(y=sysAM.mean(), color='C1', dashes=(5, 2),
            lw=0.75, zorder=-1)
ax1.axhline(y=diaPM.mean(), color='C0', lw=0.75, zorder=-1)
ax1.axhline(y=diaAM.mean(), color='C0', dashes=(5, 2),
            lw=0.75, zorder=-1)
# Formatting top graph
ax1.set_title('Blood pressure & pulse log')
ax1.set_ylabel('blood pressure (mm-Hg)')
ax1.legend(loc=(0.37, 0.43))
ax1.grid(dashes=(1, 2))
# Plot pulse
PulsePM.plot(ax=ax2, marker='o', ms=3, lw=0, color='k',
             label='PM')
PulseAM.plot(ax=ax2, marker='o', ms=3, lw=0, color='k',
             mfc='white', label='AM')
# Average values of pulse with arrows labeling them
Pulseavgs = (PulseAM.mean(), PulsePM.mean())
tavgs = ('AM average = {0:0.0f}'.format(Pulseavgs[0]),
         'PM average = {0:0.0f}'.format(Pulseavgs[1]))
for i, pulse in enumerate(Pulseavgs):
    ax2.annotate(tavgs[i], xy=(dtlab, pulse),
                 xytext=((15, -(-1)**(i)*15)),
                 textcoords='offset points',
                 arrowprops=aprops, ha='left',
                 va=ytext[-i-1])

ax2.axhline(y=PulsePM.mean(), color='k', lw=0.75, zorder=-1)
ax2.axhline(y=PulseAM.mean(), color='k', dashes=(5, 2),
            lw=0.75, zorder=-1)
# Formatting bottom graph
week = mdates.WeekdayLocator(byweekday=mdates.SU)
day = mdates.DayLocator()
ax2.xaxis.set_major_locator(week)
ax2.xaxis.set_minor_locator(day)
ax2.set_xlabel('')
ax2.set_ylabel('pulse (/min)')
ax2.legend(loc=(0.4, 0.7))
ax2.grid(dashes=(1, 2))

fig.tight_layout()
fig.savefig('./figures/BloodPressure.pdf')
fig.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2017-07-15

Read in blood pressure data from BloodPressure.xlsx,
parse in different ways, and plot.
"""
