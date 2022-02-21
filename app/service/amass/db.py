import grpc
from google.protobuf.json_format import MessageToDict
from app.protos.amass.db import db_service_pb2_grpc as pb2_grpc
from app.protos.amass.db import db_message_pb2 as pb2_msg

import logging
class DBClient(object):
    """
    Client from Amass DB Service
    """

    def __init__(self):
        self.host = "localhost"
        self.server_port = "3000"

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")

        self.stub = pb2_grpc.DBServiceStub(self.channel)
    
    def get_enum(self, domain: str = "", config: dict = None) -> pb2_msg.DBResult:
        """
        Get enum
        """
        assert(len(domain) != 0 or (len(domain) == 0 and config != None))
        
        try:
            request = pb2_msg.DBRequest(id="user-1", domain=domain, config=config)
            response = self.stub.Run(request=request)
            return MessageToDict(response.result)
        except grpc.RpcError as e:
            logging.error(e)
            raise