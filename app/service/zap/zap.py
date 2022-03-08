import logging

import requests
from fastapi import Response
from starlette.responses import JSONResponse


class ZAPClient(object):
    """
    Client for ZAP Service
    """

    def __init__(self):
        self.server = "localhost:8080/api"
        self.options = {"base": "/basescan", "full": "/fullscan"}

    def scanning(self, url: str, option: str) -> Response:
        try:
            if len(url) > 0:
                return JSONResponse(
                    status_code=200,
                    content=requests.post(
                        self.server
                        + self.options.get(
                            option, "Only 'base' and 'full' are allowed."
                        ),
                        data=url,
                    ),
                )
            else:
                return JSONResponse(
                    status_code=400, content={"message": "Invalid Request"}
                )
        except Exception as e:
            logging.error(e)
            return JSONResponse(status_code=400, content={"message": "error"})
