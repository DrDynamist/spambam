from app.services.scorer import score_email


def test_high_risk_recruiter_from_gmail():
    result = score_email(
        sender_email="globaltalentsearch@gmail.com",
        subject="Job Opportunity for Data Analyst",
        body="Hello candidate, I am a recruiter and would like to schedule an interview. Kindly reply soon."
    )

    assert result["risk"] == "HIGH"
    assert result["recruiting"] is True
    assert result["domain"] == "gmail.com"


def test_low_risk_normal_email():
    result = score_email(
        sender_email="friend@example.com",
        subject="Weekend plans",
        body="Want to hang out Saturday?"
    )

    assert result["risk"] == "LOW"
    assert result["recruiting"] is False