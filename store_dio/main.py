"""principal para criar a api"""

from fastapi import FastAPI
from store_dio.core.config import settings


class App(FastAPI):
    """app padrao"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )
        print("http://127.0.0.1:8000/docs")
        print("db: ", settings.DATABASE_URL)


app = App()
