from __future__ import annotations

import base64
import os.path
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_gmail_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w", encoding="utf-8") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def list_message_ids(service, max_results: int = 10) -> list[str]:
    response = (
        service.users()
        .messages()
        .list(userId="me", maxResults=max_results)
        .execute()
    )
    return [msg["id"] for msg in response.get("messages", [])]


def get_message(service, message_id: str) -> dict[str, Any]:
    return (
        service.users()
        .messages()
        .get(userId="me", id=message_id, format="full")
        .execute()
    )


def extract_headers(message: dict[str, Any]) -> dict[str, str]:
    headers = message.get("payload", {}).get("headers", [])
    result = {}
    for h in headers:
        name = h.get("name", "")
        value = h.get("value", "")
        result[name] = value
    return result


def extract_plain_text_body(message: dict[str, Any]) -> str:
    payload = message.get("payload", {})
    body_data = payload.get("body", {}).get("data")

    if body_data:
        return base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")

    for part in payload.get("parts", []):
        if part.get("mimeType") == "text/plain":
            data = part.get("body", {}).get("data")
            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

    return ""