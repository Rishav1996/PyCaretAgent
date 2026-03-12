import requests

data = {
    "product_category": "Beauty",
    "price": 250.0,
    "discount_percent": 10,
    "quantity_sold": 2,
    "customer_region": "Asia",
    "payment_method": "Wallet",
    "rating": 3.5,
    "review_count": 200,
    "discounted_price": 225.0,
    "total_revenue": 450.0
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
