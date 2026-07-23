from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    ENVIRONMENT: str

    MONGO_URI: str
    DATABASE_NAME: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()