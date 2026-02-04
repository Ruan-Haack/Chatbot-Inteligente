from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    
    PROJECT_NAME: str = "Chatbot Inteligente"
    SECRET_KEY: str
    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    OPENAI_API_KEY: Optional[str] = None
    APP_ENV: str = "dev"
    LOG_LEVEL: str = "info"

    # 'extra="ignore"' evita que o app quebre se houver variáveis extras no .env
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Instância única para ser importada
settings = Settings()