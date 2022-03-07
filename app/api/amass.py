import logging
import re

from fastapi import APIRouter
from fastapi.param_functions import Body
from starlette.responses import JSONResponse

from app.schemas import EnumRequestModel
from app.service.amass.db import DBClient
from app.service.amass.enum import EnumClient
from app.service.amass.viz import VizClient

enum_client = EnumClient()
db_client = DBClient()
viz_client = VizClient()

router = APIRouter()


@router.post("/enum")
def enumerate(req: EnumRequestModel = Body(...)) -> JSONResponse:
    domain = re.sub(r"^http(s)?://", "", req.domain)
    config = req.config.dict() if req.config != None else None
    try:
        result = enum_client.enumerate(domain, config=config)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})


@router.get("/db")
def get_enum_by_domain(domain: str) -> JSONResponse:
    assert domain != ""

    domain = re.sub(r"^http(s)?://", "", domain)

    try:
        result = db_client.get_enum(domain=domain)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})


@router.get("/db/latest")
def get_latest_enum() -> JSONResponse:
    try:
        result = db_client.get_enum(config={"latest": True})
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})


# --- VIZ ---
@router.get("/viz/graphistry")
def get_graphistry(domain: str) -> JSONResponse:

    domain = re.sub(r"^http(s)?://", "", domain)

    try:
        result = viz_client.get_graphistry(domain)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})
