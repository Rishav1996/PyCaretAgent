import requests
import json

url = "http://localhost:5000/predict"
data = {
    "AveragePrice": 1.5,
    "TotalVolume": 100000.0,
    "Mango_4046": 50000.0,
    "Mango_4225": 20000.0,
    "Mango_4770": 10000.0,
    "SmallBags": 5000.0,
    "LargeBags": 5000.0,
    "TotalBags": 10000.0
}

response = requests.post(url, json=data)
print(response.json())
