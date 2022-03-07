from fastapi import FastAPI

from .api import service

app = FastAPI()

app.include_router(
    service.router,
    prefix="/api/service",
    responses={404: {"message": "Not Found"}},
)
