
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ollama_endpoint: str = "http://localhost:11434"
    model_name: str = "trixbot-chat"
    max_history_length: int = 10

    class Config:
        env_file = ".env"
    
settings = Settings()