from fastapi import APIRouter
from app.models.request_models import EmailRequest
from app.models.response_models import EmailScoreResponse, HealthResponse
from app.services.scorer import score_email

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok")


@router.post("/score-email", response_model=EmailScoreResponse)
def score_email_route(payload: EmailRequest) -> EmailScoreResponse:
    result = score_email(
        sender_email=payload.sender_email,
        subject=payload.subject,
        body=payload.body
    )
    return EmailScoreResponse(**result)