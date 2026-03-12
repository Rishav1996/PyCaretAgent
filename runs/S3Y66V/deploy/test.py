import requests

url = 'http://localhost:5000/predict'
data = {
    "age": 22,
    "gender": "Female",
    "study_hours_per_day": 5.0,
    "sleep_hours": 7.0,
    "phone_usage_hours": 4.0,
    "social_media_hours": 2.0,
    "youtube_hours": 1.0,
    "gaming_hours": 1.0,
    "breaks_per_day": 5,
    "coffee_intake_mg": 200,
    "exercise_minutes": 60,
    "assignments_completed": 10,
    "attendance_percentage": 90.0,
    "stress_level": 3,
    "focus_score": 80,
    "final_grade": 85.0
}
response = requests.post(url, json=data)
print(response.json())
