# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/protos/amass/enum/enum_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from app.protos.amass.enum import enum_message_pb2 as app_dot_protos_dot_amass_dot_enum_dot_enum__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/protos/amass/enum/enum_service.proto',
  package='enum',
  syntax='proto3',
  serialized_options=b'Z0github.com/kofeebrian/capamass/protos/amass/enum',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(app/protos/amass/enum/enum_service.proto\x12\x04\x65num\x1a(app/protos/amass/enum/enum_message.proto2=\n\x0b\x45numService\x12.\n\x03Run\x12\x11.enum.EnumRequest\x1a\x12.enum.EnumResponse\"\x00\x42\x32Z0github.com/kofeebrian/capamass/protos/amass/enumb\x06proto3'
  ,
  dependencies=[app_dot_protos_dot_amass_dot_enum_dot_enum__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_ENUMSERVICE = _descriptor.ServiceDescriptor(
  name='EnumService',
  full_name='enum.EnumService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=92,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='enum.EnumService.Run',
    index=0,
    containing_service=None,
    input_type=app_dot_protos_dot_amass_dot_enum_dot_enum__message__pb2._ENUMREQUEST,
    output_type=app_dot_protos_dot_amass_dot_enum_dot_enum__message__pb2._ENUMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENUMSERVICE)

DESCRIPTOR.services_by_name['EnumService'] = _ENUMSERVICE

# @@protoc_insertion_point(module_scope)