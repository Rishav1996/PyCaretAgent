import requests
import json

url = "http://localhost:5000/predict"
data = {"fh": 7}  # Request 7 days forecast

response = requests.post(url, json=data)
print(response.json())
