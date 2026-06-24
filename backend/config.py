from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "ResearchForge"
    DEBUG: bool = True

    # Database (we'll fill in real values in Phase 1.4)
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/researchforge"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()