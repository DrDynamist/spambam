from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_score_email_endpoint():
    payload = {
        "sender_email": "globaltalentsearch@gmail.com",
        "subject": "Job Opportunity",
        "body": "Hello, I am a recruiter. Kindly reply to schedule an interview."
    }

    response = client.post("/api/v1/score-email", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["risk"] in {"HIGH", "MEDIUM", "LOW"}
    assert data["domain"] == "gmail.com"