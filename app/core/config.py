from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "DATABASE_URL"
    POSTGRES_DB: str = "POSTGRES_DB"
    POSTGRES_USER: str = "POSTGRES_USER"
    POSTGRES_PASSWORD: str = "POSTGRES_PASSWORD"
    POSTGRES_HOST: str = "POSTGRES_HOST"
    POSTGRES_PORT: int = "POSTGRES_PORT"

settings = Settings()