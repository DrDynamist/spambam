from app.services.domain_checker import get_sender_domain, is_free_email_domain


def test_extract_domain():
    assert get_sender_domain("person@gmail.com") == "gmail.com"


def test_free_email_domain_true():
    assert is_free_email_domain("gmail.com") is True


def test_free_email_domain_false():
    assert is_free_email_domain("company.com") is False