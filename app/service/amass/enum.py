import datetime
import logging
from typing import Any, Text

import grpc
from google.protobuf.json_format import MessageToDict

from app.protos.amass.enum import enum_message_pb2 as pb2_msg
from app.protos.amass.enum import enum_service_pb2_grpc as pb2_grpc


class EnumClient(object):
    """
    Client for Amass Enum Service
    """

    def __init__(self):
        self.host = "localhost"
        self.server_port = "3000"

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")

        self.stub = pb2_grpc.EnumServiceStub(self.channel)

    def enumerate(self, domain: str, config: dict = None) -> dict[Text, Any]:
        """
        Perform enumeration
        """

        assert len(domain) > 0

        try:
            id = int(datetime.datetime.now().timestamp())
            request = pb2_msg.EnumRequest(id=str(id), domain=domain, config=config)
            response = self.stub.Run(request=request)
        except grpc.RpcError as e:
            logging.error(f"Enumeration failed with {e}")
            raise
        else:
            logging.info("Enumeration finished")
            return MessageToDict(response)
