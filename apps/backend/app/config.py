from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str = "dev"
    frontend_url: str = "http://localhost:3000"
    backend_url: str = "http://localhost:8000"
    db_url: str
    redis_url: str
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"
    aws_region: str = "us-east-1"

    class Config:
        env_file = "../../.env"
        env_file_encoding = "utf-8"


settings = Settings()
