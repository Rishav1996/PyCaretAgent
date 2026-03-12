from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.regression import load_model, predict_model

app = FastAPI()

model = load_model('final_regression_model')

class DataModel(BaseModel):
    age: int
    gender: str
    study_hours_per_day: float
    sleep_hours: float
    phone_usage_hours: float
    social_media_hours: float
    youtube_hours: float
    gaming_hours: float
    breaks_per_day: int
    coffee_intake_mg: int
    exercise_minutes: int
    assignments_completed: int
    attendance_percentage: float
    stress_level: int
    focus_score: int
    final_grade: float

@app.post('/predict')
async def predict(data: DataModel):
    df = pd.DataFrame([data.dict()])
    prediction = predict_model(model, data=df)
    return {'prediction': float(prediction['prediction_label'][0])}
