# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/product_type_level.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/product_type_level.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v0.enumsB\025ProductTypeLevelProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums\352\002!Google::Ads::GoogleAds::V0::Enums'),
  serialized_pb=_b('\n<google/ads/googleads_v0/proto/enums/product_type_level.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xb2\x01\n\x14ProductTypeLevelEnum\"\x99\x01\n\x10ProductTypeLevel\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0fPRODUCT_TYPE_L1\x10\x02\x12\x13\n\x0fPRODUCT_TYPE_L2\x10\x03\x12\x13\n\x0fPRODUCT_TYPE_L3\x10\x04\x12\x13\n\x0fPRODUCT_TYPE_L4\x10\x05\x12\x13\n\x0fPRODUCT_TYPE_L5\x10\x06\x42\xea\x01\n!com.google.ads.googleads.v0.enumsB\x15ProductTypeLevelProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enums\xea\x02!Google::Ads::GoogleAds::V0::Enumsb\x06proto3')
)



_PRODUCTTYPELEVELENUM_PRODUCTTYPELEVEL = _descriptor.EnumDescriptor(
  name='ProductTypeLevel',
  full_name='google.ads.googleads.v0.enums.ProductTypeLevelEnum.ProductTypeLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TYPE_L1', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TYPE_L2', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TYPE_L3', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TYPE_L4', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TYPE_L5', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=121,
  serialized_end=274,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTTYPELEVELENUM_PRODUCTTYPELEVEL)


_PRODUCTTYPELEVELENUM = _descriptor.Descriptor(
  name='ProductTypeLevelEnum',
  full_name='google.ads.googleads.v0.enums.ProductTypeLevelEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRODUCTTYPELEVELENUM_PRODUCTTYPELEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=274,
)

_PRODUCTTYPELEVELENUM_PRODUCTTYPELEVEL.containing_type = _PRODUCTTYPELEVELENUM
DESCRIPTOR.message_types_by_name['ProductTypeLevelEnum'] = _PRODUCTTYPELEVELENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductTypeLevelEnum = _reflection.GeneratedProtocolMessageType('ProductTypeLevelEnum', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTTYPELEVELENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.product_type_level_pb2'
  ,
  __doc__ = """Level of the type of a product offer.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.ProductTypeLevelEnum)
  ))
_sym_db.RegisterMessage(ProductTypeLevelEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
