import logging
from starlette.responses import JSONResponse
from fastapi import Response
import requests


class WAPPClient(object):
    """
    Client for Wappalyzer Service
    """

    def __init__(self):
        self.server = "http://wapp-service:3000"

    def scanning(self, url: str) -> Response:
        try:
            if len(url) > 0:
                response = requests.get(f"{self.server}/?url={url}")
                return JSONResponse(status_code=200, content=response.json())
            else:
                return JSONResponse(
                    status_code=400, content={"message": "Invalid Request"}
                )
        except Exception as e:
            logging.error(e)
            return JSONResponse(status_code=400, content={"message": "error"})
