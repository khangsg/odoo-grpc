# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbase.proto\"$\n\x0eProductRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\x05\"5\n\x0fProductResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cpublic_price\x18\x02 \x01(\t2?\n\x08Products\x12\x33\n\x0eGetProductInfo\x12\x0f.ProductRequest\x1a\x10.ProductResponseb\x06proto3'
)




_PRODUCTREQUEST = _descriptor.Descriptor(
  name='ProductRequest',
  full_name='ProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='ProductRequest.product_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=14,
  serialized_end=50,
)


_PRODUCTRESPONSE = _descriptor.Descriptor(
  name='ProductResponse',
  full_name='ProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ProductResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_price', full_name='ProductResponse.public_price', index=1,
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
  ],
  serialized_start=52,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['ProductRequest'] = _PRODUCTREQUEST
DESCRIPTOR.message_types_by_name['ProductResponse'] = _PRODUCTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductRequest = _reflection.GeneratedProtocolMessageType('ProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTREQUEST,
  '__module__' : 'base_pb2'
  # @@protoc_insertion_point(class_scope:ProductRequest)
  })
_sym_db.RegisterMessage(ProductRequest)

ProductResponse = _reflection.GeneratedProtocolMessageType('ProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTRESPONSE,
  '__module__' : 'base_pb2'
  # @@protoc_insertion_point(class_scope:ProductResponse)
  })
_sym_db.RegisterMessage(ProductResponse)



_PRODUCTS = _descriptor.ServiceDescriptor(
  name='Products',
  full_name='Products',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=170,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetProductInfo',
    full_name='Products.GetProductInfo',
    index=0,
    containing_service=None,
    input_type=_PRODUCTREQUEST,
    output_type=_PRODUCTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTS)

DESCRIPTOR.services_by_name['Products'] = _PRODUCTS

# @@protoc_insertion_point(module_scope)
