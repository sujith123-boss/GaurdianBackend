from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = Field(default="Guardian AI", env="APP_NAME")
    APP_VERSION: str = Field(default="1.0.0", env="APP_VERSION")
    DEBUG: bool = Field(default=True, env="DEBUG")

    # Database settings
    DATABASE_URL: str = Field(default="postgresql+asyncpg://user:password@localhost/dbname", env="DATABASE_URL")

    # Redis settings
    REDIS_URL: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")

    # Security settings
    SECRET_KEY: str = Field(default="dummy-secret-key", env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # Logging settings
    LOG_LEVEL: str = Field(default="DEBUG", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()