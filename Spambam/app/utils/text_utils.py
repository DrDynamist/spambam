import re


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def keyword_hits(text: str, keywords: set[str]) -> list[str]:
    hits = []
    for keyword in sorted(keywords):
        if keyword in text:
            hits.append(keyword)
    return hits