from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    secret_key: str = "change-this-to-a-long-random-secret-key"
    database_path: str = "./pocketsmart.db"
    max_upload_mb: int = 5

    class Config:
        env_file = ".env"
        extra="ignore"


settings = Settings()