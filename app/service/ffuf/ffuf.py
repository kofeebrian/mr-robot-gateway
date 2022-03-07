import logging
from flask import request
from starlette.responses import JSONResponse
from fastapi import Response
import requests

class FFUFClient(object):
    """
    Client for FFUF Service
    """

    def __init__(self):
        self.server = "localhost:8000/api/scan"

    def fuzzing(self, url: str) -> Response:
        try:
            if len(url) > 0:
                return JSONResponse(
                    status_code = 200,
                    content = requests.post(self.server, data=url)
                )
            else:
                return JSONResponse(
                    status_code = 400,
                    content = {"message": "Invalid Request"}
                )
        except Exception as e:
            logging.error(e)
            return JSONResponse(
                status_code=400,
                content={"message": "error"}
            )