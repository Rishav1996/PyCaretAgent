from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.anomaly import load_model, predict_model
import os

app = FastAPI()

# Load model
model = load_model('iforest_mango_model')

class DataModel(BaseModel):
    AveragePrice: float
    TotalVolume: float
    Mango_4046: float
    Mango_4225: float
    Mango_4770: float
    SmallBags: float
    LargeBags: float
    TotalBags: float

@app.post('/predict')
async def predict(data: DataModel):
    df = pd.DataFrame([data.dict()])
    # Rename columns to match training schema
    df.columns = ['AveragePrice', 'Total Volume', 'Mango_4046', 'Mango_4225', 'Mango_4770', 'Small Bags', 'Large Bags', 'Total Bags']
    prediction = predict_model(model, data=df)
    return {"anomaly": int(prediction['Anomaly'].iloc[0]), "score": float(prediction['Anomaly_Score'].iloc[0])}
