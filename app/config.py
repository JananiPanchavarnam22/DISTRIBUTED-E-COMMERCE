import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    CELERY_DATABASE_URL: str =os.getenv("CELERY_DATABASE_URL")
    REDIS_URL: str =os.getenv("REDIS_URL")
settings = Settings()