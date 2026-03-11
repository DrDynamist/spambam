from app.services.rules import FREE_EMAIL_DOMAINS
from app.utils.email_utils import extract_domain


def get_sender_domain(sender_email: str) -> str:
    return extract_domain(sender_email)


def is_free_email_domain(domain: str) -> bool:
    return domain.lower() in FREE_EMAIL_DOMAINS