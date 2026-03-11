def extract_domain(sender_email: str) -> str:
    sender_email = sender_email.strip().lower()
    if "@" not in sender_email:
        return ""
    return sender_email.split("@")[-1]