from fastapi import APIRouter, Body, Response
from starlette.responses import JSONResponse
import logging, os, json

router = APIRouter()

@router.get("/")
def hello():
    return {"Hello": "World"}
    