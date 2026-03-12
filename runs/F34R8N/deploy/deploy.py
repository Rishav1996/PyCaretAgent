from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.time_series import load_model, predict_model

app = FastAPI()

class DataModel(BaseModel):
    fh: int = 1  # Forecast horizon

model = load_model('final_ts_model')

@app.post('/predict')
async def predict(data: DataModel):
    predictions = predict_model(model, fh=data.fh)
    return predictions.to_dict()
