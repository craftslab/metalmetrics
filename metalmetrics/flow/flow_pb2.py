# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="flow.proto",
    package="flow",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\nflow.proto\x12\x04\x66low"\x1e\n\x0b\x46lowRequest\x12\x0f\n\x07message\x18\x01 \x01(\t"\x1c\n\tFlowReply\x12\x0f\n\x07message\x18\x01 \x01(\t2=\n\tFlowProto\x12\x30\n\x08SendFlow\x12\x11.flow.FlowRequest\x1a\x0f.flow.FlowReply"\x00\x62\x06proto3',
)


_FLOWREQUEST = _descriptor.Descriptor(
    name="FlowRequest",
    full_name="flow.FlowRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="flow.FlowRequest.message",
            index=0,
            number=1,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=20,
    serialized_end=50,
)


_FLOWREPLY = _descriptor.Descriptor(
    name="FlowReply",
    full_name="flow.FlowReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="flow.FlowReply.message",
            index=0,
            number=1,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=52,
    serialized_end=80,
)

DESCRIPTOR.message_types_by_name["FlowRequest"] = _FLOWREQUEST
DESCRIPTOR.message_types_by_name["FlowReply"] = _FLOWREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowRequest = _reflection.GeneratedProtocolMessageType(
    "FlowRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOWREQUEST,
        "__module__": "flow_pb2"
        # @@protoc_insertion_point(class_scope:flow.FlowRequest)
    },
)
_sym_db.RegisterMessage(FlowRequest)

FlowReply = _reflection.GeneratedProtocolMessageType(
    "FlowReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOWREPLY,
        "__module__": "flow_pb2"
        # @@protoc_insertion_point(class_scope:flow.FlowReply)
    },
)
_sym_db.RegisterMessage(FlowReply)


_FLOWPROTO = _descriptor.ServiceDescriptor(
    name="FlowProto",
    full_name="flow.FlowProto",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=82,
    serialized_end=143,
    methods=[
        _descriptor.MethodDescriptor(
            name="SendFlow",
            full_name="flow.FlowProto.SendFlow",
            index=0,
            containing_service=None,
            input_type=_FLOWREQUEST,
            output_type=_FLOWREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_FLOWPROTO)

DESCRIPTOR.services_by_name["FlowProto"] = _FLOWPROTO

# @@protoc_insertion_point(module_scope)