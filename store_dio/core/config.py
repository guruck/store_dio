"""configuracao para aplicacao"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """definicoes da aplicacao"""

    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"

    DATABASE_URL: str = ""  # verificar se captura do ENV

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
