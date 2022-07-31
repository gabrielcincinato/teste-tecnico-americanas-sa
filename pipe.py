from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer, MinMaxScaler
import pandas as pd
import numpy as np

def transform(arr):
    arrs = np.array(arr).reshape(1, -1)
    X_train = pd.read_csv('dados/X.csv')
    power_scaler = PowerTransformer()
    min_max_scaler = MinMaxScaler()
    pipeline = Pipeline(steps=[('p', power_scaler), ('m', min_max_scaler)])
    pipeline.fit(X_train)
    return pipeline.transform(arrs)
