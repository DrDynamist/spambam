from app.config import settings
from app.services.domain_checker import get_sender_domain, is_free_email_domain
from app.services.recruiter_detector import detect_recruiting_language
from app.services.rules import (
    CHAT_APP_TERMS,
    CHAT_APP_PENALTY,
    COMPANY_CLAIM_SCORE,
    COMPANY_CLAIM_TERMS,
    FREE_DOMAIN_PENALTY,
    RECRUITING_SIGNAL_SCORE,
    SUSPICIOUS_KEYWORDS,
    SUSPICIOUS_WORDING_PENALTY,
)
from app.utils.text_utils import normalize_text, keyword_hits


def determine_risk_label(score: int) -> str:
    if score >= settings.high_risk_threshold:
        return "HIGH"
    if score >= settings.medium_risk_threshold:
        return "MEDIUM"
    return "LOW"


def score_email(sender_email: str, subject: str, body: str) -> dict:
    text = normalize_text(f"{subject} {body}")
    domain = get_sender_domain(sender_email)

    score = 0
    reasons: list[str] = []

    recruiting, recruiting_hits = detect_recruiting_language(subject, body)
    suspicious_hits = keyword_hits(text, SUSPICIOUS_KEYWORDS)
    chat_hits = keyword_hits(text, CHAT_APP_TERMS)
    company_claim_hits = keyword_hits(text, COMPANY_CLAIM_TERMS)

    if recruiting:
        score += RECRUITING_SIGNAL_SCORE
        reasons.append("Recruiting-related language detected")

    if company_claim_hits:
        score += COMPANY_CLAIM_SCORE
        reasons.append("Claims company, agency, or hiring-team affiliation")

    if recruiting and is_free_email_domain(domain):
        score += FREE_DOMAIN_PENALTY
        reasons.append(f"Recruiting email sent from free email domain: {domain}")

    if chat_hits:
        score += CHAT_APP_PENALTY
        reasons.append(
            f"Requests or references off-platform chat tools: {', '.join(chat_hits)}"
        )

    for hit in suspicious_hits:
        score += SUSPICIOUS_WORDING_PENALTY
        reasons.append(f"Contains suspicious wording: {hit}")

    risk = determine_risk_label(score)

    return {
        "risk": risk,
        "score": score,
        "domain": domain,
        "recruiting": recruiting,
        "recruiting_hits": recruiting_hits,
        "suspicious_hits": suspicious_hits,
        "reasons": reasons,
    }