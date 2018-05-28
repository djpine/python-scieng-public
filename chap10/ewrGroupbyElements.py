import pandas as pd

ewr = pd.read_csv('ewrFlights20180516.csv')

for airln, grp in ewr.groupby(ewr['Airline']):
    print('\nairln = {}: \ngrp:'.format(airln))
    print(grp)

    if airln == 'AVIANCA':
        break
