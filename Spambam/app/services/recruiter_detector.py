from app.services.rules import RECRUITER_KEYWORDS
from app.utils.text_utils import normalize_text, keyword_hits


def detect_recruiting_language(subject: str, body: str) -> tuple[bool, list[str]]:
    text = normalize_text(f"{subject} {body}")
    hits = keyword_hits(text, RECRUITER_KEYWORDS)
    return len(hits) > 0, hits