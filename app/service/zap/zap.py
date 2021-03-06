import logging

import requests
from fastapi import Response
from starlette.responses import JSONResponse


class ZAPClient(object):
    """
    Client for ZAP Service
    """

    def __init__(self):
        self.server = "http://zap-service:8000/api"
        self.options = {"base": "/basescan", "full": "/fullscan"}

    def scanning(self, url: str, option: str) -> Response:
        try:
            if len(url) > 0:
                response = requests.post(
                    self.server
                    + self.options.get(option, "Only 'base' and 'full' are allowed."),
                    json={"url": url},
                )
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
