from fastapi import APIRouter, Body, Response
from starlette.responses import JSONResponse
from app.schemas import Test_input
import logging, os, json

router = APIRouter()

# Example of GET api
@router.get("/")
def hello():
    return {"Hello": "World"}
    
# Example of POST api
@router.post("/scan", status_code=200)
def test(req_body: Test_input = Body(...)) -> Response:
    try:
        if req_body:
            return JSONResponse(
                status_code = 200,
                content = {
                    "message": req_body.message
                }
            )
        else:
            return JSONResponse(
                status_code = 400,
                content = {
                    "message": "Request not found"
                }
            )
    except Exception as e:
        logging.error(e)
        return JSONResponse(
            status_code = 400,
            content = {
                "message": "error"
            }
        )
