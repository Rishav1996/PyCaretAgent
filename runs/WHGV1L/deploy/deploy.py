import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from pycaret.classification import load_model, predict_model

app = FastAPI()

class DataModel(BaseModel):
    cgpa: float
    backlogs: int
    college_tier: str
    country: str
    university_ranking_band: str
    internship_count: int
    aptitude_score: float
    communication_score: float
    specialization: str
    industry: str
    internship_quality_score: float

model = load_model('final_pipeline')

@app.post('/predict')
async def predict(data: DataModel):
    df = pd.DataFrame([data.dict()])
    prediction = predict_model(model, data=df)
    return {"prediction": prediction['prediction_label'].iloc[0]}
