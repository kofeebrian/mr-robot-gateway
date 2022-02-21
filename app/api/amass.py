from fastapi import APIRouter, Body, Response
from starlette.responses import JSONResponse
import logging, os, json

from app.service.amass.db import DBClient


client = DBClient()

router = APIRouter(prefix="/db")

@router.get("/")
def get_enum_by_domain(domain: str):
  try:
    result = client.get_enum(domain=domain)
    return JSONResponse(status_code=200, content=result)
  except Exception as e:  
    print(e)
    return JSONResponse(status_code=400, content={
      "message": "error"
    })

@router.get("/latest")
def get_latest_enum() -> JSONResponse:
  try:
    result = client.get_enum(config={ "latest": True })
    return JSONResponse(status_code=200, content=result)
  except Exception as e:  
    print(e)
    return JSONResponse(status_code=400, content={
      "message": "error"
    })
