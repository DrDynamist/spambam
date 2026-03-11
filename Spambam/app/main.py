from fastapi import FastAPI
from app.config import settings
from app.api.routes import router as api_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0"
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root() -> dict:
    return {
        "message": settings.app_name,
        "env": settings.app_env,
        "docs": "/docs"
    }