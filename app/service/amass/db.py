import grpc
from app.protos.amass.db import db_service_pb2_grpc as pb2_grpc
from app.protos.amass.db import db_message_pb2 as pb2_msg

class DBClient(object):
    """
    Client from Amass DB Service
    """

    def __init__(self):
        self.host = "localhost"
        self.server_port = "50051"

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")

        self.stub = pb2_grpc.DBServiceStub(self.channel)

    def get_latest_enum(self):
        """
        Get the latest enumeration result
        ex. Use after run enumeration
        """

        # TODO: use proper id
        request = pb2_msg.DBRequest( id="user-1", config={ "latest": True })

        response = self.stub.Run(request=request)
        print(response)
