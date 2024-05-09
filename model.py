from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd
import numpy as np

x = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

lr = LinearRegression()
lr.fit(x, y)

model_path = 'models/model.pkl'
joblib.dump(lr, model_path)
print(f"Model dumped at {model_path}")
