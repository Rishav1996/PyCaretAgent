import requests

data = {
    "cgpa": 8.5,
    "backlogs": 0,
    "college_tier": "Tier 1",
    "country": "USA",
    "university_ranking_band": "Top 100",
    "internship_count": 2,
    "aptitude_score": 90.0,
    "communication_score": 85.0,
    "specialization": "Data Science",
    "industry": "Consulting",
    "internship_quality_score": 8.0
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
