"""
The purpose of this script is to do a test split based on 5 times. Accordingly, we provide the following groups of training / test sets based on the years of our samples:
• 2010-2011 for testing; 2012-2019 for training.
• 2012-2013 for testing; 2010-2011 and 2014-2019 for training.
• 2014-2015 for testing; 2010-2013 and 2016-2019 for training.
• 2016-2017 for testing; 2010-2015 and 2018-2019 for training.
• 2018-2019 for testing; 2010-2017 for training.

This script creates the folder “Training and test” that contains the data mentioned above.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import GroupKFold
from sklearn.model_selection import GroupShuffleSplit


def z_score(X):
    dataLista = X.copy()
    cols = list(dataLista.columns)
    
    for col in cols:
        if dataLista[col].dtypes.kind in 'f':
            dataLista[col] = ((dataLista[col] - dataLista[col].mean())/dataLista[col].std(ddof=0))
    
    return dataLista


dataAll = pd.read_csv("06.2-DATA SET FOR SOLAR FLARE PREDICTION.csv", sep=";")


dataAll['FlareNumber'] = dataAll['FlareNumber'].replace([1, 2], 1)
dataAll['FlareNumber'] = dataAll['FlareNumber'].replace([3, 4], 2)


dataAll['YEAR']=pd.DatetimeIndex(dataAll['T_REC']).year

dataAll = dataAll.drop('NOAA_AR', axis=1)
dataAll = dataAll.drop('QUALITY', axis=1)
dataAll = dataAll.drop('Longitude', axis=1)
dataAll = dataAll.drop('Latitude', axis=1)
dataAll = dataAll.drop('T_REC', axis=1)


X = dataAll.drop('FlareNumber', axis=1)
y = dataAll['FlareNumber']

count=1
for x in range(2010,2019,2):
    print(x)
    test_data = dataAll.query(f'YEAR == {x} or YEAR == {x+1}')
    train_data = dataAll.query(f'YEAR != {x} and YEAR != {x+1}')

    # REMOVE YEAR FROM DATA ALL
    # test_data = test_data.drop('YEAR', axis=1)
    # train_data = train_data.drop('YEAR', axis=1)

    test_data= z_score(test_data)
    train_data= z_score(train_data)

    test_data.to_csv(f"07.1-Training and test\\{count}-fold-test.csv", sep=';', encoding='utf-8', index=False, header=True)
    train_data.to_csv(f"07.1-Training and test\\{count}-fold-train.csv", sep=';', encoding='utf-8', index=False, header=True)

    count=count+1

