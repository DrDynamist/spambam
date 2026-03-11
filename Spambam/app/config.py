from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Job Scam Detector API"
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    debug: bool = True
    high_risk_threshold: int = 6
    medium_risk_threshold: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()