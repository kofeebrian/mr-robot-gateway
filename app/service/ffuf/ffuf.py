import logging
from starlette.responses import JSONResponse
from fastapi import Response
import requests


class FFUFClient(object):
    """
    Client for FFUF Service
    """

    def __init__(self):
        self.server = "http://ffuf-service:8000/api/scan"

    def fuzzing(self, url: str) -> Response:
        try:
            if len(url) > 0:
                response = requests.post(self.server, json={"url": url})
                return JSONResponse(
                    status_code=response.status_code, content=response.json()
                )
            else:
                return JSONResponse(
                    status_code=400, content={"message": "Invalid Request"}
                )
        except Exception as e:
            logging.error(e)
            return JSONResponse(status_code=400, content={"message": "error"})
