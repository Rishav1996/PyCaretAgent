from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.clustering import load_model, predict_model

app = FastAPI()

# Load model
model = load_model('amazon_clustering_model')

class DataModel(BaseModel):
    product_category: str
    price: float
    discount_percent: int
    quantity_sold: int
    customer_region: str
    payment_method: str
    rating: float
    review_count: int
    discounted_price: float
    total_revenue: float

@app.post('/predict')
def predict(data: DataModel):
    df = pd.DataFrame([data.dict()])
    prediction = predict_model(model, data=df)
    return {"cluster": prediction['Cluster'].iloc[0]}
