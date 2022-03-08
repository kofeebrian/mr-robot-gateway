import logging
import re

from fastapi import APIRouter, Response
from fastapi.param_functions import Body
from starlette.responses import JSONResponse

from app.schemas import EnumRequestModel, ZapRequestModel
from app.service.amass.db import DBClient
from app.service.amass.enum import EnumClient
from app.service.amass.viz import VizClient
from app.service.ffuf.ffuf import FFUFClient
from app.service.nmap.nmap import NmapClient
from app.service.wapp.wapp import WAPPClient
from app.service.zap.zap import ZAPClient

# Client for each service
enum_client = EnumClient()
ffuf_client = FFUFClient()
nmap_client = NmapClient()
wapp_client = WAPPClient()
viz_client = VizClient()
zap_client = ZAPClient()
db_client = DBClient()

router = APIRouter()

# --- ZAP ---
@router.post("/zap/scan")
async def zap_scan(req: ZapRequestModel = Body(...)) -> Response:
    url = req.url
    option = req.option if req.option != None else "base"

    return zap_client.scanning(url, option)
    
@router.post("/amass/enum")
def enumerate(req: EnumRequestModel = Body(...)) -> JSONResponse:
    domain = re.sub(r"^http(s)?://", "", req.domain)
    config = req.config.dict() if req.config != None else None
    try:
        result = enum_client.enumerate(domain, config=config)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})


@router.get("/amass/db")
def get_enum_by_domain(domain: str) -> JSONResponse:
    assert domain != ""

    domain = re.sub(r"^http(s)?://", "", domain)

    try:
        result = db_client.get_enum(domain=domain)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})


@router.get("/amass/db/latest")
def get_latest_enum() -> JSONResponse:
    try:
        result = db_client.get_enum(config={"latest": True})
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})


# --- VIZ ---
@router.get("/amass/viz/graphistry")
def get_graphistry(domain: str) -> JSONResponse:

    domain = re.sub(r"^http(s)?://", "", domain)

    try:
        result = viz_client.get_graphistry(domain)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "error"})
