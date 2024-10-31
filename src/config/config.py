from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
JWT_KEY = os.getenv("JWT_CODE")


class Settings:

    @property
    def url_return(self):
        return (f"postgresql+asyncpg://{DB_USER}:"
                f"{DB_PASSWORD}@db:5432/{DB_PASSWORD}")

    @property
    def jwt_return(self):
        return f"{JWT_KEY}"


settings = Settings()
url = settings.url_return
jwt_key = settings.jwt_return
