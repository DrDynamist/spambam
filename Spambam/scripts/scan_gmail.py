from app.services.gmail_client import (
    get_gmail_service,
    list_message_ids,
    get_message,
    extract_headers,
    extract_plain_text_body,
)
from app.services.scorer import score_email


def main():
    service = get_gmail_service()
    message_ids = list_message_ids(service, max_results=10)

    for msg_id in message_ids:
        msg = get_message(service, msg_id)
        headers = extract_headers(msg)

        sender = headers.get("From", "")
        subject = headers.get("Subject", "")
        body = extract_plain_text_body(msg)

        # crude sender parsing for now
        sender_email = sender
        if "<" in sender and ">" in sender:
            sender_email = sender.split("<")[-1].replace(">", "").strip()

        result = score_email(
            sender_email=sender_email,
            subject=subject,
            body=body,
        )

        print("=" * 80)
        print("FROM:", sender)
        print("SUBJECT:", subject)
        print("RESULT:", result)


if __name__ == "__main__":
    main()