from app.services.recruiter_detector import detect_recruiting_language


def test_detect_recruiting_language_true():
    subject = "Job Opportunity"
    body = "Hello, I am a recruiter and want to schedule an interview."
    result, hits = detect_recruiting_language(subject, body)

    assert result is True
    assert "recruiter" in hits
    assert "interview" in hits


def test_detect_recruiting_language_false():
    subject = "Dinner plans"
    body = "Let's grab food tonight."
    result, hits = detect_recruiting_language(subject, body)

    assert result is False
    assert hits == []