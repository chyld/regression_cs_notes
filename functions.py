def clean(df):
    df = df.copy()
    df = df.loc[:, ['YearMade', 'MachineHoursCurrentMeter']]
    mhcm_mean = df.MachineHoursCurrentMeter.mean()
    df.MachineHoursCurrentMeter = df.MachineHoursCurrentMeter.fillna(mhcm_mean)
    return df
