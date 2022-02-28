# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/protos/amass/viz/viz_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/protos/amass/viz/viz_message.proto',
  package='viz',
  syntax='proto3',
  serialized_options=b'Z/github.com/kofeebrian/capamass/protos/amass/viz',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&app/protos/amass/viz/viz_message.proto\x12\x03viz\"\x1f\n\tVizConfig\x12\x12\n\ngraphistry\x18\x01 \x01(\x08\"3\n\x04\x45\x64ge\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0b\n\x03\x64st\x18\x02 \x01(\t\x12\x11\n\tedgeTitle\x18\x03 \x01(\t\"J\n\x08\x42indings\x12\x13\n\x0bsourceField\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65stinationField\x18\x02 \x01(\t\x12\x0f\n\x07idField\x18\x03 \x01(\t\"o\n\x05Label\x12\x0c\n\x04node\x18\x01 \x01(\t\x12\x12\n\npointLabel\x18\x02 \x01(\t\x12\x12\n\npointTitle\x18\x03 \x01(\t\x12\x12\n\npointColor\x18\x04 \x01(\x04\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x0e\n\x06source\x18\x06 \x01(\t\"\x85\x01\n\x10GraphistryResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x1f\n\x08\x62indings\x18\x03 \x01(\x0b\x32\r.viz.Bindings\x12\x18\n\x05graph\x18\x04 \x03(\x0b\x32\t.viz.Edge\x12\x1a\n\x06labels\x18\x05 \x03(\x0b\x32\n.viz.Label\"8\n\nVizRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x06\x64omain\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_domain\"n\n\x0bVizResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x06\x64omain\x18\x02 \x01(\tH\x01\x88\x01\x01\x12)\n\x08g_result\x18\x03 \x01(\x0b\x32\x15.viz.GraphistryResultH\x00\x42\x08\n\x06resultB\t\n\x07_domainB1Z/github.com/kofeebrian/capamass/protos/amass/vizb\x06proto3'
)




_VIZCONFIG = _descriptor.Descriptor(
  name='VizConfig',
  full_name='viz.VizConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='graphistry', full_name='viz.VizConfig.graphistry', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=78,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='viz.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='viz.Edge.src', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst', full_name='viz.Edge.dst', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edgeTitle', full_name='viz.Edge.edgeTitle', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=131,
)


_BINDINGS = _descriptor.Descriptor(
  name='Bindings',
  full_name='viz.Bindings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceField', full_name='viz.Bindings.sourceField', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destinationField', full_name='viz.Bindings.destinationField', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idField', full_name='viz.Bindings.idField', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=207,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='viz.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='viz.Label.node', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pointLabel', full_name='viz.Label.pointLabel', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pointTitle', full_name='viz.Label.pointTitle', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pointColor', full_name='viz.Label.pointColor', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='viz.Label.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='viz.Label.source', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=320,
)


_GRAPHISTRYRESULT = _descriptor.Descriptor(
  name='GraphistryResult',
  full_name='viz.GraphistryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='viz.GraphistryResult.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='viz.GraphistryResult.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bindings', full_name='viz.GraphistryResult.bindings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph', full_name='viz.GraphistryResult.graph', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='viz.GraphistryResult.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=456,
)


_VIZREQUEST = _descriptor.Descriptor(
  name='VizRequest',
  full_name='viz.VizRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='viz.VizRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='viz.VizRequest.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_domain', full_name='viz.VizRequest._domain',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=458,
  serialized_end=514,
)


_VIZRESPONSE = _descriptor.Descriptor(
  name='VizResponse',
  full_name='viz.VizResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='viz.VizResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='viz.VizResponse.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='g_result', full_name='viz.VizResponse.g_result', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='result', full_name='viz.VizResponse.result',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_domain', full_name='viz.VizResponse._domain',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=516,
  serialized_end=626,
)

_GRAPHISTRYRESULT.fields_by_name['bindings'].message_type = _BINDINGS
_GRAPHISTRYRESULT.fields_by_name['graph'].message_type = _EDGE
_GRAPHISTRYRESULT.fields_by_name['labels'].message_type = _LABEL
_VIZREQUEST.oneofs_by_name['_domain'].fields.append(
  _VIZREQUEST.fields_by_name['domain'])
_VIZREQUEST.fields_by_name['domain'].containing_oneof = _VIZREQUEST.oneofs_by_name['_domain']
_VIZRESPONSE.fields_by_name['g_result'].message_type = _GRAPHISTRYRESULT
_VIZRESPONSE.oneofs_by_name['result'].fields.append(
  _VIZRESPONSE.fields_by_name['g_result'])
_VIZRESPONSE.fields_by_name['g_result'].containing_oneof = _VIZRESPONSE.oneofs_by_name['result']
_VIZRESPONSE.oneofs_by_name['_domain'].fields.append(
  _VIZRESPONSE.fields_by_name['domain'])
_VIZRESPONSE.fields_by_name['domain'].containing_oneof = _VIZRESPONSE.oneofs_by_name['_domain']
DESCRIPTOR.message_types_by_name['VizConfig'] = _VIZCONFIG
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['Bindings'] = _BINDINGS
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['GraphistryResult'] = _GRAPHISTRYRESULT
DESCRIPTOR.message_types_by_name['VizRequest'] = _VIZREQUEST
DESCRIPTOR.message_types_by_name['VizResponse'] = _VIZRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VizConfig = _reflection.GeneratedProtocolMessageType('VizConfig', (_message.Message,), {
  'DESCRIPTOR' : _VIZCONFIG,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.VizConfig)
  })
_sym_db.RegisterMessage(VizConfig)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), {
  'DESCRIPTOR' : _EDGE,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.Edge)
  })
_sym_db.RegisterMessage(Edge)

Bindings = _reflection.GeneratedProtocolMessageType('Bindings', (_message.Message,), {
  'DESCRIPTOR' : _BINDINGS,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.Bindings)
  })
_sym_db.RegisterMessage(Bindings)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.Label)
  })
_sym_db.RegisterMessage(Label)

GraphistryResult = _reflection.GeneratedProtocolMessageType('GraphistryResult', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHISTRYRESULT,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.GraphistryResult)
  })
_sym_db.RegisterMessage(GraphistryResult)

VizRequest = _reflection.GeneratedProtocolMessageType('VizRequest', (_message.Message,), {
  'DESCRIPTOR' : _VIZREQUEST,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.VizRequest)
  })
_sym_db.RegisterMessage(VizRequest)

VizResponse = _reflection.GeneratedProtocolMessageType('VizResponse', (_message.Message,), {
  'DESCRIPTOR' : _VIZRESPONSE,
  '__module__' : 'app.protos.amass.viz.viz_message_pb2'
  # @@protoc_insertion_point(class_scope:viz.VizResponse)
  })
_sym_db.RegisterMessage(VizResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)