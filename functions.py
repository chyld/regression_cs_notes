# Used to prepare dataframes for analysis

class Cleaner:
    def __init__(self, columns):
        self.columns = columns

    def fit(self, train):
        self.mhcm_mean = train.MachineHoursCurrentMeter.mean()

    def transform(self, df):
        df = df.copy()
        df = df.loc[:, self.columns]
        df.MachineHoursCurrentMeter = df.MachineHoursCurrentMeter.fillna(self.mhcm_mean)
        return df
