import pandas as pd

ewr = pd.read_csv('ewrFlights20180516.csv')

for airln, grp in ewr.groupby(ewr['Airline']):
    print('\nairln = {}: \ngrp:'.format(airln))
    print(grp)

    if airln == 'AVIANCA':
        break

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-19

Demonstrates how to itereate3 over groups using
Pandas.
"""
