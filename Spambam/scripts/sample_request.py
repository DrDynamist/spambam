import requests

payload = {
    "sender_email": "globaltalentsearch@gmail.com",
    "subject": "Job Opportunity for Data Analyst",
    "body": "Hello candidate, I am a recruiter and would like to schedule an interview. Kindly reply soon."
}

response = requests.post("http://127.0.0.1:8000/api/v1/score-email", json=payload, timeout=10)
print(response.status_code)
print(response.json())