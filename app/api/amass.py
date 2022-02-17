from fastapi import APIRouter, Body, Response
from starlette.responses import JSONResponse
import logging, os, json

from app.service.amass.db import DBClient


# client = DBClient()

router = APIRouter(prefix="/db")

@router.post("/latest")
def get_latest_enum() -> JSONResponse:
  return JSONResponse(
    status_code=200,
    content = {
      "Hello": "World"
    }
  )
  # client.get_latest_enum()