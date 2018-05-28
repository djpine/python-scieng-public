from datetime import timedelta
i_A = ewr.columns.get_loc("Arrival_time")  # i_A  = 6
i_Ap = ewr.columns.get_loc("A_day")        # i_Ap = 7
i_S = ewr.columns.get_loc("Scheduled")     # i_S  = 8
i_Sp = ewr.columns.get_loc("S_day")        # i_Sp = 9
for i in range(ewr.shape[0]):
    if ewr.iloc[i, i_Ap] >= 1:
        ewr.iloc[i, i_A] += timedelta(days=ewr.iloc[i, i_Ap])
    if ewr.iloc[i, i_Sp] >= 1:
        ewr.iloc[i, i_S] += timedelta(days=ewr.iloc[i, i_Sp])
