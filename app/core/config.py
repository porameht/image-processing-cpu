from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Settings
    API_TITLE: str = "Background Remover API"
    API_HOST: str
    API_PORT: int
    
    # Directory Settings
    TEMP_DIR: str = "temp"
    OUTPUT_DIR: str = "output"
    
    # Cloudinary Settings
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    
    class Config:
        env_file = ".env"

settings = Settings() 