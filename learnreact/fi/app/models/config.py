from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):

    DATABASE_URL: str
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama"
    class Config:
        env_file = ".env"


settings = Settings()