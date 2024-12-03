from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    mongodb_url: str = "your_mongodb_atlas_connection_string"
    database_name: str = "student_management"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()