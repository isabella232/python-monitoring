# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/common.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=b"\n\030com.google.monitoring.v3B\013CommonProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3\352\002\035Google::Cloud::Monitoring::V3",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-google/cloud/monitoring_v3/proto/common.proto\x12\x14google.monitoring.v3\x1a\x1dgoogle/api/distribution.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaa\x01\n\nTypedValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12\x36\n\x12\x64istribution_value\x18\x05 \x01(\x0b\x32\x18.google.api.DistributionH\x00\x42\x07\n\x05value"l\n\x0cTimeInterval\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\xad\x07\n\x0b\x41ggregation\x12\x33\n\x10\x61lignment_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x45\n\x12per_series_aligner\x18\x02 \x01(\x0e\x32).google.monitoring.v3.Aggregation.Aligner\x12G\n\x14\x63ross_series_reducer\x18\x04 \x01(\x0e\x32).google.monitoring.v3.Aggregation.Reducer\x12\x17\n\x0fgroup_by_fields\x18\x05 \x03(\t"\x8b\x03\n\x07\x41ligner\x12\x0e\n\nALIGN_NONE\x10\x00\x12\x0f\n\x0b\x41LIGN_DELTA\x10\x01\x12\x0e\n\nALIGN_RATE\x10\x02\x12\x15\n\x11\x41LIGN_INTERPOLATE\x10\x03\x12\x14\n\x10\x41LIGN_NEXT_OLDER\x10\x04\x12\r\n\tALIGN_MIN\x10\n\x12\r\n\tALIGN_MAX\x10\x0b\x12\x0e\n\nALIGN_MEAN\x10\x0c\x12\x0f\n\x0b\x41LIGN_COUNT\x10\r\x12\r\n\tALIGN_SUM\x10\x0e\x12\x10\n\x0c\x41LIGN_STDDEV\x10\x0f\x12\x14\n\x10\x41LIGN_COUNT_TRUE\x10\x10\x12\x15\n\x11\x41LIGN_COUNT_FALSE\x10\x18\x12\x17\n\x13\x41LIGN_FRACTION_TRUE\x10\x11\x12\x17\n\x13\x41LIGN_PERCENTILE_99\x10\x12\x12\x17\n\x13\x41LIGN_PERCENTILE_95\x10\x13\x12\x17\n\x13\x41LIGN_PERCENTILE_50\x10\x14\x12\x17\n\x13\x41LIGN_PERCENTILE_05\x10\x15\x12\x18\n\x14\x41LIGN_PERCENT_CHANGE\x10\x17"\xb1\x02\n\x07Reducer\x12\x0f\n\x0bREDUCE_NONE\x10\x00\x12\x0f\n\x0bREDUCE_MEAN\x10\x01\x12\x0e\n\nREDUCE_MIN\x10\x02\x12\x0e\n\nREDUCE_MAX\x10\x03\x12\x0e\n\nREDUCE_SUM\x10\x04\x12\x11\n\rREDUCE_STDDEV\x10\x05\x12\x10\n\x0cREDUCE_COUNT\x10\x06\x12\x15\n\x11REDUCE_COUNT_TRUE\x10\x07\x12\x16\n\x12REDUCE_COUNT_FALSE\x10\x0f\x12\x18\n\x14REDUCE_FRACTION_TRUE\x10\x08\x12\x18\n\x14REDUCE_PERCENTILE_99\x10\t\x12\x18\n\x14REDUCE_PERCENTILE_95\x10\n\x12\x18\n\x14REDUCE_PERCENTILE_50\x10\x0b\x12\x18\n\x14REDUCE_PERCENTILE_05\x10\x0c*\x9e\x01\n\x0e\x43omparisonType\x12\x1a\n\x16\x43OMPARISON_UNSPECIFIED\x10\x00\x12\x11\n\rCOMPARISON_GT\x10\x01\x12\x11\n\rCOMPARISON_GE\x10\x02\x12\x11\n\rCOMPARISON_LT\x10\x03\x12\x11\n\rCOMPARISON_LE\x10\x04\x12\x11\n\rCOMPARISON_EQ\x10\x05\x12\x11\n\rCOMPARISON_NE\x10\x06*a\n\x0bServiceTier\x12\x1c\n\x18SERVICE_TIER_UNSPECIFIED\x10\x00\x12\x16\n\x12SERVICE_TIER_BASIC\x10\x01\x12\x18\n\x14SERVICE_TIER_PREMIUM\x10\x02\x1a\x02\x18\x01\x42\xc3\x01\n\x18\x63om.google.monitoring.v3B\x0b\x43ommonProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3',
    dependencies=[
        google_dot_api_dot_distribution__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)

_COMPARISONTYPE = _descriptor.EnumDescriptor(
    name="ComparisonType",
    full_name="google.monitoring.v3.ComparisonType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_GT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_GE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_LT",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_LE",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_EQ",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPARISON_NE",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1395,
    serialized_end=1553,
)
_sym_db.RegisterEnumDescriptor(_COMPARISONTYPE)

ComparisonType = enum_type_wrapper.EnumTypeWrapper(_COMPARISONTYPE)
_SERVICETIER = _descriptor.EnumDescriptor(
    name="ServiceTier",
    full_name="google.monitoring.v3.ServiceTier",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SERVICE_TIER_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVICE_TIER_BASIC",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVICE_TIER_PREMIUM",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=b"\030\001",
    serialized_start=1555,
    serialized_end=1652,
)
_sym_db.RegisterEnumDescriptor(_SERVICETIER)

ServiceTier = enum_type_wrapper.EnumTypeWrapper(_SERVICETIER)
COMPARISON_UNSPECIFIED = 0
COMPARISON_GT = 1
COMPARISON_GE = 2
COMPARISON_LT = 3
COMPARISON_LE = 4
COMPARISON_EQ = 5
COMPARISON_NE = 6
SERVICE_TIER_UNSPECIFIED = 0
SERVICE_TIER_BASIC = 1
SERVICE_TIER_PREMIUM = 2


_AGGREGATION_ALIGNER = _descriptor.EnumDescriptor(
    name="Aligner",
    full_name="google.monitoring.v3.Aggregation.Aligner",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ALIGN_NONE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_DELTA",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_RATE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_INTERPOLATE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_NEXT_OLDER",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_MIN",
            index=5,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_MAX",
            index=6,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_MEAN",
            index=7,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_COUNT",
            index=8,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_SUM",
            index=9,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_STDDEV",
            index=10,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_COUNT_TRUE",
            index=11,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_COUNT_FALSE",
            index=12,
            number=24,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_FRACTION_TRUE",
            index=13,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_PERCENTILE_99",
            index=14,
            number=18,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_PERCENTILE_95",
            index=15,
            number=19,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_PERCENTILE_50",
            index=16,
            number=20,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_PERCENTILE_05",
            index=17,
            number=21,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALIGN_PERCENT_CHANGE",
            index=18,
            number=23,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=689,
    serialized_end=1084,
)
_sym_db.RegisterEnumDescriptor(_AGGREGATION_ALIGNER)

_AGGREGATION_REDUCER = _descriptor.EnumDescriptor(
    name="Reducer",
    full_name="google.monitoring.v3.Aggregation.Reducer",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="REDUCE_NONE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_MEAN",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_MIN",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_MAX",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_SUM",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_STDDEV",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_COUNT",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_COUNT_TRUE",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_COUNT_FALSE",
            index=8,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_FRACTION_TRUE",
            index=9,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_PERCENTILE_99",
            index=10,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_PERCENTILE_95",
            index=11,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_PERCENTILE_50",
            index=12,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REDUCE_PERCENTILE_05",
            index=13,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1087,
    serialized_end=1392,
)
_sym_db.RegisterEnumDescriptor(_AGGREGATION_REDUCER)


_TYPEDVALUE = _descriptor.Descriptor(
    name="TypedValue",
    full_name="google.monitoring.v3.TypedValue",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="bool_value",
            full_name="google.monitoring.v3.TypedValue.bool_value",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="int64_value",
            full_name="google.monitoring.v3.TypedValue.int64_value",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="double_value",
            full_name="google.monitoring.v3.TypedValue.double_value",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="string_value",
            full_name="google.monitoring.v3.TypedValue.string_value",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="distribution_value",
            full_name="google.monitoring.v3.TypedValue.distribution_value",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="value",
            full_name="google.monitoring.v3.TypedValue.value",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=168,
    serialized_end=338,
)


_TIMEINTERVAL = _descriptor.Descriptor(
    name="TimeInterval",
    full_name="google.monitoring.v3.TimeInterval",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="end_time",
            full_name="google.monitoring.v3.TimeInterval.end_time",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="start_time",
            full_name="google.monitoring.v3.TimeInterval.start_time",
            index=1,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=340,
    serialized_end=448,
)


_AGGREGATION = _descriptor.Descriptor(
    name="Aggregation",
    full_name="google.monitoring.v3.Aggregation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="alignment_period",
            full_name="google.monitoring.v3.Aggregation.alignment_period",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="per_series_aligner",
            full_name="google.monitoring.v3.Aggregation.per_series_aligner",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="cross_series_reducer",
            full_name="google.monitoring.v3.Aggregation.cross_series_reducer",
            index=2,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="group_by_fields",
            full_name="google.monitoring.v3.Aggregation.group_by_fields",
            index=3,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_AGGREGATION_ALIGNER, _AGGREGATION_REDUCER],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=451,
    serialized_end=1392,
)

_TYPEDVALUE.fields_by_name[
    "distribution_value"
].message_type = google_dot_api_dot_distribution__pb2._DISTRIBUTION
_TYPEDVALUE.oneofs_by_name["value"].fields.append(
    _TYPEDVALUE.fields_by_name["bool_value"]
)
_TYPEDVALUE.fields_by_name["bool_value"].containing_oneof = _TYPEDVALUE.oneofs_by_name[
    "value"
]
_TYPEDVALUE.oneofs_by_name["value"].fields.append(
    _TYPEDVALUE.fields_by_name["int64_value"]
)
_TYPEDVALUE.fields_by_name["int64_value"].containing_oneof = _TYPEDVALUE.oneofs_by_name[
    "value"
]
_TYPEDVALUE.oneofs_by_name["value"].fields.append(
    _TYPEDVALUE.fields_by_name["double_value"]
)
_TYPEDVALUE.fields_by_name[
    "double_value"
].containing_oneof = _TYPEDVALUE.oneofs_by_name["value"]
_TYPEDVALUE.oneofs_by_name["value"].fields.append(
    _TYPEDVALUE.fields_by_name["string_value"]
)
_TYPEDVALUE.fields_by_name[
    "string_value"
].containing_oneof = _TYPEDVALUE.oneofs_by_name["value"]
_TYPEDVALUE.oneofs_by_name["value"].fields.append(
    _TYPEDVALUE.fields_by_name["distribution_value"]
)
_TYPEDVALUE.fields_by_name[
    "distribution_value"
].containing_oneof = _TYPEDVALUE.oneofs_by_name["value"]
_TIMEINTERVAL.fields_by_name[
    "end_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEINTERVAL.fields_by_name[
    "start_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AGGREGATION.fields_by_name[
    "alignment_period"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_AGGREGATION.fields_by_name["per_series_aligner"].enum_type = _AGGREGATION_ALIGNER
_AGGREGATION.fields_by_name["cross_series_reducer"].enum_type = _AGGREGATION_REDUCER
_AGGREGATION_ALIGNER.containing_type = _AGGREGATION
_AGGREGATION_REDUCER.containing_type = _AGGREGATION
DESCRIPTOR.message_types_by_name["TypedValue"] = _TYPEDVALUE
DESCRIPTOR.message_types_by_name["TimeInterval"] = _TIMEINTERVAL
DESCRIPTOR.message_types_by_name["Aggregation"] = _AGGREGATION
DESCRIPTOR.enum_types_by_name["ComparisonType"] = _COMPARISONTYPE
DESCRIPTOR.enum_types_by_name["ServiceTier"] = _SERVICETIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TypedValue = _reflection.GeneratedProtocolMessageType(
    "TypedValue",
    (_message.Message,),
    {
        "DESCRIPTOR": _TYPEDVALUE,
        "__module__": "google.cloud.monitoring_v3.proto.common_pb2",
        "__doc__": """A single strongly-typed value.
  
  Attributes:
      value:
          The typed value field.
      bool_value:
          A Boolean value: ``true`` or ``false``.
      int64_value:
          A 64-bit integer. Its range is approximately ±9.2x1018.
      double_value:
          A 64-bit double-precision floating-point number. Its magnitude
          is approximately ±10±300 and it has 16 significant digits of
          precision.
      string_value:
          A variable-length string value.
      distribution_value:
          A distribution value.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.TypedValue)
    },
)
_sym_db.RegisterMessage(TypedValue)

TimeInterval = _reflection.GeneratedProtocolMessageType(
    "TimeInterval",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMEINTERVAL,
        "__module__": "google.cloud.monitoring_v3.proto.common_pb2",
        "__doc__": """A closed time interval. It extends from the start time to the end
  time, and includes both: ``[startTime, endTime]``. Valid time
  intervals depend on the ```MetricKind`` <https://cloud.google.com/moni
  toring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind>`__ of
  the metric value. In no case can the end time be earlier than the
  start time.  -  For a ``GAUGE`` metric, the ``startTime`` value is
  technically    optional; if no value is specified, the start time
  defaults to the    value of the end time, and the interval represents
  a single point in    time. If both start and end times are specified,
  they must be    identical. Such an interval is valid only for
  ``GAUGE`` metrics,    which are point-in-time measurements.  -  For
  ``DELTA`` and ``CUMULATIVE`` metrics, the start time must be
  earlier than the end time.  -  In all cases, the start time of the
  next interval must be at least a    millisecond after the end time of
  the previous interval. Because the    interval is closed, if the start
  time of a new interval is the same    as the end time of the previous
  interval, data written at the new    start time could overwrite data
  written at the previous end time.
  
  Attributes:
      end_time:
          Required. The end of the time interval.
      start_time:
          Optional. The beginning of the time interval. The default
          value for the start time is the end time. The start time must
          not be later than the end time.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.TimeInterval)
    },
)
_sym_db.RegisterMessage(TimeInterval)

Aggregation = _reflection.GeneratedProtocolMessageType(
    "Aggregation",
    (_message.Message,),
    {
        "DESCRIPTOR": _AGGREGATION,
        "__module__": "google.cloud.monitoring_v3.proto.common_pb2",
        "__doc__": """Describes how to combine multiple time series to provide a different
  view of the data. Aggregation of time series is done in two steps.
  First, each time series in the set is *aligned* to the same time
  interval boundaries, then the set of time series is optionally
  *reduced* in number.  Alignment consists of applying the
  ``per_series_aligner`` operation to each time series after its data
  has been divided into regular ``alignment_period`` time intervals.
  This process takes *all* of the data points in an alignment period,
  applies a mathematical transformation such as averaging, minimum,
  maximum, delta, etc., and converts them into a single data point per
  period.  Reduction is when the aligned and transformed time series can
  optionally be combined, reducing the number of time series through
  similar mathematical transformations. Reduction involves applying a
  ``cross_series_reducer`` to all the time series, optionally sorting
  the time series into subsets with ``group_by_fields``, and applying
  the reducer to each subset.  The raw time series data can contain a
  huge amount of information from multiple sources. Alignment and
  reduction transforms this mass of data into a more manageable and
  representative collection of data, for example “the 95% latency across
  the average of all tasks in a cluster”. This representative data can
  be more easily graphed and comprehended, and the individual time
  series data is still available for later drilldown. For more details,
  see `Filtering and aggregation
  <https://cloud.google.com/monitoring/api/v3/aggregation>`__.
  
  Attributes:
      alignment_period:
          The ``alignment_period`` specifies a time interval, in
          seconds, that is used to divide the data in all the [time
          series][google.monitoring.v3.TimeSeries] into consistent
          blocks of time. This will be done before the per-series
          aligner can be applied to the data.  The value must be at
          least 60 seconds. If a per-series aligner other than
          ``ALIGN_NONE`` is specified, this field is required or an
          error is returned. If no per-series aligner is specified, or
          the aligner ``ALIGN_NONE`` is specified, then this field is
          ignored.
      per_series_aligner:
          An ``Aligner`` describes how to bring the data points in a
          single time series into temporal alignment. Except for
          ``ALIGN_NONE``, all alignments cause all the data points in an
          ``alignment_period`` to be mathematically grouped together,
          resulting in a single data point for each ``alignment_period``
          with end timestamp at the end of the period.  Not all
          alignment operations may be applied to all time series. The
          valid choices depend on the ``metric_kind`` and ``value_type``
          of the original time series. Alignment can change the
          ``metric_kind`` or the ``value_type`` of the time series.
          Time series data must be aligned in order to perform cross-
          time series reduction. If ``cross_series_reducer`` is
          specified, then ``per_series_aligner`` must be specified and
          not equal to ``ALIGN_NONE`` and ``alignment_period`` must be
          specified; otherwise, an error is returned.
      cross_series_reducer:
          The reduction operation to be used to combine time series into
          a single time series, where the value of each data point in
          the resulting series is a function of all the already aligned
          values in the input time series.  Not all reducer operations
          can be applied to all time series. The valid choices depend on
          the ``metric_kind`` and the ``value_type`` of the original
          time series. Reduction can yield a time series with a
          different ``metric_kind`` or ``value_type`` than the input
          time series.  Time series data must first be aligned (see
          ``per_series_aligner``) in order to perform cross-time series
          reduction. If ``cross_series_reducer`` is specified, then
          ``per_series_aligner`` must be specified, and must not be
          ``ALIGN_NONE``. An ``alignment_period`` must also be
          specified; otherwise, an error is returned.
      group_by_fields:
          The set of fields to preserve when ``cross_series_reducer`` is
          specified. The ``group_by_fields`` determine how the time
          series are partitioned into subsets prior to applying the
          aggregation operation. Each subset contains time series that
          have the same value for each of the grouping fields. Each
          individual time series is a member of exactly one subset. The
          ``cross_series_reducer`` is applied to each subset of time
          series. It is not possible to reduce across different resource
          types, so this field implicitly contains ``resource.type``.
          Fields not specified in ``group_by_fields`` are aggregated
          away. If ``group_by_fields`` is not specified and all the time
          series have the same resource type, then the time series are
          aggregated into a single output time series. If
          ``cross_series_reducer`` is not defined, this field is
          ignored.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.Aggregation)
    },
)
_sym_db.RegisterMessage(Aggregation)


DESCRIPTOR._options = None
_SERVICETIER._options = None
# @@protoc_insertion_point(module_scope)
