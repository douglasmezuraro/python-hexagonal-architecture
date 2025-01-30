from pydantic_settings import BaseSettings


class Options(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"
