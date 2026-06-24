from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "ResearchForge"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str

    # Storage
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str
    SUPABASE_BUCKET: str = "papers"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()