from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np

from template import ReggressionInput 

app = FastAPI()
lr = joblib.load("models/model.pkl")

@app.get('/')
def index():
    return {'message': 'linear reggresion'}

@app.post('/car/predict')
def predict_y(data: ReggressionInput):
    data = data.dict()
    x_values = data['x_values']
    x_values = [[x] for x in x_values]
    prediction = lr.predict(x_values)
    return {'prediction': list(prediction)}

