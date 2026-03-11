from pydantic import BaseModel
from typing import List


class HealthResponse(BaseModel):
    status: str


class EmailScoreResponse(BaseModel):
    risk: str
    score: int
    domain: str
    recruiting: bool
    recruiting_hits: List[str]
    suspicious_hits: List[str]
    reasons: List[str]