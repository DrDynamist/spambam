from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


def load_lines(filename: str) -> set[str]:
    path = DATA_DIR / filename
    with path.open("r", encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip() and not line.strip().startswith("#")
        }


FREE_EMAIL_DOMAINS = load_lines("free_email_domains.txt")
RECRUITER_KEYWORDS = load_lines("recruiter_keywords.txt")
SUSPICIOUS_KEYWORDS = load_lines("suspicious_keywords.txt")

RECRUITING_SIGNAL_SCORE = 2
FREE_DOMAIN_PENALTY = 6
CHAT_APP_PENALTY = 4
SUSPICIOUS_WORDING_PENALTY = 1
COMPANY_CLAIM_SCORE = 2

CHAT_APP_TERMS = {"telegram", "whatsapp", "signal", "skype"}
COMPANY_CLAIM_TERMS = {
    "we are hiring",
    "our client",
    "on behalf of",
    "talent acquisition",
    "staffing firm",
    "recruitment agency",
    "hiring team",
    "human resources",
    "hr department"
}