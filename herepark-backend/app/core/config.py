from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'herePark'
    app_description: str = 'herePark backend service'

    DB_URI: PostgresDsn = PostgresDsn(
        'postgresql+asyncpg://user:pass@hostname:5432/db'
    )

    SECRET_KEY: str = 'secret'
    JWT_ALGORITHM: str = 'HS256'
    TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_prefix='HP_', env_file='.env')


settings: Settings = Settings()
