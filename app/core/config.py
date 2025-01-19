from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Settings
    API_TITLE: str = "Background Remover API"
    API_HOST: str
    API_PORT: int
    
    # Directory Settings
    TEMP_DIR: str = "temp"
    OUTPUT_DIR: str = "output"
    
    class Config:
        env_file = ".env"

settings = Settings() 