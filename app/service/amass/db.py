import logging
import datetime
from typing import Any, Text

import grpc
from google.protobuf.json_format import MessageToDict

from app.protos.amass.db import db_message_pb2 as pb2_msg
from app.protos.amass.db import db_service_pb2_grpc as pb2_grpc


class DBClient(object):
    """
    Client for Amass DB Service
    """

    def __init__(self):
        self.host = "localhost"
        self.server_port = "3000"

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")

        self.stub = pb2_grpc.DBServiceStub(self.channel)

    def get_enum(self, domain: str = "", config: dict = None) -> dict[Text, Any]:
        """
        Get enum
        """
        assert len(domain) != 0 or (len(domain) == 0 and config != None)

        try:
            id = int(datetime.datetime.now().timestamp() * 1e6)
            request = pb2_msg.DBRequest(id=str(id), domain=domain, config=config)
            response = self.stub.Run(request=request)
        except grpc.RpcError as e:
            logging.error(f"Enumeration get failed with {e}")
            raise
        else:
            logging.info("Enumeration received")
            return MessageToDict(response.result)
