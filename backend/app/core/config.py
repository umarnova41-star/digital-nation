from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/digital_nation"
    KEYCLOAK_ISSUER: str = "https://keycloak.example.com/realms/digital-nation"
    KEYCLOAK_CLIENT_ID: str = "web-client"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
