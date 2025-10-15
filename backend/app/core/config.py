from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "AI Recipe Genie"
    GEMINI_API_KEY: str = "YOUR_GEMINI_API_KEY"
    DATABASE_URL: str = "sqlite:///./test.db"
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_REDIRECT_URI: Optional[str] = None
    SECRET_KEY: str = "your-super-secret-key"
    API_V1_STR: str = "/api/v1"
    TESTING: bool = False

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
