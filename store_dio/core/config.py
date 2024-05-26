"""configuracao para aplicacao"""

import os
from pydantic import ConfigDict, BaseModel  # , SettingsConfigDict
from dotenv import load_dotenv, dotenv_values
from typing import Optional


class Settings(BaseModel):
    """definicoes da aplicacao"""

    model_config = ConfigDict(extra="allow")

    load_dotenv()

    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"

    DATABASE_URL: Optional[str] = os.getenv(
        "DATABASE_URL"
    )  # verificar se captura do ENV
    OTHER: dict = dotenv_values()


settings = Settings()
