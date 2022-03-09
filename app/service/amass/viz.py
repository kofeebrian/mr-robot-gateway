import datetime
import logging

import grpc
from google.protobuf.json_format import MessageToDict

from app.protos.amass.viz import viz_message_pb2 as pb2_msg
from app.protos.amass.viz import viz_service_pb2_grpc as pb2_grpc


class VizClient(object):
    """
    Client for Amass Viz Service
    """

    def __init__(self) -> None:
        self.host = "amass-service"
        self.server_port = "3000"

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")

        self.stub = pb2_grpc.VizServiceStub(self.channel)

    def get_graphistry(self, domain: str = ""):
        """
        Perform getting graphistry format graph (JSON)
        """

        try:
            id = int(datetime.datetime.now().timestamp())
            request = pb2_msg.VizRequest(id=str(id), domain=domain)
            response = self.stub.GetGraphistry(request=request)
        except grpc.RpcError as e:
            logging.error(f"GetGraphistry failed with: {e}")
            raise
        else:
            logging.info("GetGraphistry done")
            return MessageToDict(response)
