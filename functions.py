# Used to prepare dataframes for analysis

import numpy as np
from sklearn.metrics import make_scorer

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

def rmsle_temp(actual, predictions):
    log_diff = np.log(predictions+1) - np.log(actual+1)
    return np.sqrt(np.mean(log_diff**2))

rmsle = make_scorer(rmsle_temp, greater_is_better=False)
