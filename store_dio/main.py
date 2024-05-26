"""principal para criar a api"""

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from store_dio.core.config import settings
from store_dio.routers import api_router


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
        print("st: ", settings.OTHER["DB_URL"])


app = App()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Get the original 'detail' list of errors
    details = exc.errors()
    modified_details = []
    # Replace 'msg' with 'message' for each error
    for error in details:
        if "Field required" == error["msg"] and "missing" == error["type"]:
            modified_details.append(
                {
                    "loc": error["loc"],
                    "message": "Campo requerido",
                    "type": "faltando",
                }
            )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": modified_details}),
    )


app.include_router(api_router)
