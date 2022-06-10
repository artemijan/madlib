from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse
from api import routes

__all__ = ["app"]

app = FastAPI()
app.include_router(routes.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    _request: Request,
    exc: RequestValidationError,  # handle validation errors as 400 BAd request instead of 422
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
