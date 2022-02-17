# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import db_message_pb2 as protos_dot_amass_dot_db_dot_db__message__pb2


class DBServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Run = channel.unary_unary(
                '/db.DBService/Run',
                request_serializer=protos_dot_amass_dot_db_dot_db__message__pb2.DBRequest.SerializeToString,
                response_deserializer=protos_dot_amass_dot_db_dot_db__message__pb2.DBResponse.FromString,
                )


class DBServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Run(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=protos_dot_amass_dot_db_dot_db__message__pb2.DBRequest.FromString,
                    response_serializer=protos_dot_amass_dot_db_dot_db__message__pb2.DBResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'db.DBService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db.DBService/Run',
            protos_dot_amass_dot_db_dot_db__message__pb2.DBRequest.SerializeToString,
            protos_dot_amass_dot_db_dot_db__message__pb2.DBResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
