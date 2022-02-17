from fastapi import FastAPI
from .api import test
from .api import amass

app = FastAPI()

# Example for creating API's router

# app.include_router(
#     test.router,
#     prefix="/api",
#     responses={404: {"message": "Not Found"}},
# )

app.include_router(
    amass.router,
    prefix="/api/amass",
    responses={404: {"message": "Not Found"}},
)