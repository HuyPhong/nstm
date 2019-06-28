# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='services.proto',
  package='com.nextsmarty.nstm.rpc',
  syntax='proto3',
  serialized_options=_b('\210\001\001'),
  serialized_pb=_b('\n\x0eservices.proto\x12\x17\x63om.nextsmarty.nstm.rpc\"0\n\tTaskDescr\x12\x10\n\x08taskName\x18\x01 \x01(\t\x12\x11\n\tremoteUri\x18\x02 \x01(\t\"6\n\x0f\x44oneTaskRequest\x12\x10\n\x08taskName\x18\x01 \x01(\t\x12\x11\n\tisSuccess\x18\x02 \x01(\x08\"<\n\x0f\x44oneTaskRespone\x12)\n\x03\x61\x63k\x18\x01 \x01(\x0e\x32\x1c.com.nextsmarty.nstm.rpc.Ack\"!\n\rDeleteRequest\x12\x10\n\x08taskName\x18\x01 \x01(\t\">\n\x11\x44\x65leteTaskRespone\x12)\n\x03\x61\x63k\x18\x01 \x01(\x0e\x32\x1c.com.nextsmarty.nstm.rpc.Ack\"J\n\x11SubmitTaskRequest\x12\x35\n\ttaskDescr\x18\x01 \x01(\x0b\x32\".com.nextsmarty.nstm.rpc.TaskDescr\">\n\x11SubmitTaskRespone\x12)\n\x03\x61\x63k\x18\x01 \x01(\x0e\x32\x1c.com.nextsmarty.nstm.rpc.Ack\"`\n\x0fPullTaskRequest\x12;\n\x07metrics\x18\x01 \x01(\x0b\x32*.com.nextsmarty.nstm.rpc.AvailableResource\x12\x10\n\x08workerId\x18\x02 \x01(\t\"s\n\x0fPullTaskRespone\x12\x35\n\ttaskDescr\x18\x01 \x01(\x0b\x32\".com.nextsmarty.nstm.rpc.TaskDescr\x12)\n\x03\x61\x63k\x18\x02 \x01(\x0e\x32\x1c.com.nextsmarty.nstm.rpc.Ack\" \n\x11\x41vailableResource\x12\x0b\n\x03gpu\x18\x01 \x01(\x05\"F\n\nWorkerDesc\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x0b\n\x03gpu\x18\x03 \x01(\x05\x12\x0f\n\x07\x63puInfo\x18\x04 \x01(\t\"*\n\nMasterDesc\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x10\n\x08grpcPort\x18\x02 \x01(\x05\")\n\x15WorkerRegisterRequest\x12\x10\n\x08workerId\x18\x01 \x01(\t\"B\n\x15WorkerRegisterRespone\x12)\n\x03\x61\x63k\x18\x01 \x01(\x0e\x32\x1c.com.nextsmarty.nstm.rpc.Ack*\x89\x02\n\x03\x41\x63k\x12\x12\n\x0eSUBMIT_SUCCESS\x10\x00\x12\x19\n\x15SUBMIT_FAILURE_EXISTS\x10\x01\x12\x12\n\x0e\x44\x45LETE_SUCCESS\x10\x02\x12\"\n\x1e\x44\x45LETE_FAILURE_TASK_NOT_EXISTS\x10\x03\x12\x0e\n\nNOT_DEFINE\x10\x04\x12\x14\n\x10REGISTER_SUCCESS\x10\x05\x12\x11\n\rREGISTER_FAIL\x10\x06\x12\x15\n\x11PULL_TASK_SUCCESS\x10\x07\x12\x1d\n\x19PULL_TASK_NO_TASK_SASTIFY\x10\x08\x12\x15\n\x11\x44ONE_TASK_SUCCESS\x10\t\x12\x15\n\x11\x44ONE_TASK_FAILURE\x10\n*:\n\nTaskStatus\x12\x0b\n\x07RUNNING\x10\x00\x12\r\n\tDONE_FAIL\x10\x01\x12\x10\n\x0c\x44ONE_SUCCESS\x10\x02\x32\x84\x04\n\x04Nstm\x12`\n\x08PullTask\x12(.com.nextsmarty.nstm.rpc.PullTaskRequest\x1a(.com.nextsmarty.nstm.rpc.PullTaskRespone\"\x00\x12`\n\x08\x44oneTask\x12(.com.nextsmarty.nstm.rpc.DoneTaskRequest\x1a(.com.nextsmarty.nstm.rpc.DoneTaskRespone\"\x00\x12l\n\x08Register\x12..com.nextsmarty.nstm.rpc.WorkerRegisterRequest\x1a..com.nextsmarty.nstm.rpc.WorkerRegisterRespone\"\x00\x12\x66\n\nSubmitTask\x12*.com.nextsmarty.nstm.rpc.SubmitTaskRequest\x1a*.com.nextsmarty.nstm.rpc.SubmitTaskRespone\"\x00\x12\x62\n\nDeleteTask\x12&.com.nextsmarty.nstm.rpc.DeleteRequest\x1a*.com.nextsmarty.nstm.rpc.DeleteTaskRespone\"\x00\x42\x03\x88\x01\x01\x62\x06proto3')
)

_ACK = _descriptor.EnumDescriptor(
  name='Ack',
  full_name='com.nextsmarty.nstm.rpc.Ack',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_FAILURE_EXISTS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_SUCCESS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_FAILURE_TASK_NOT_EXISTS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_DEFINE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_SUCCESS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_FAIL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PULL_TASK_SUCCESS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PULL_TASK_NO_TASK_SASTIFY', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE_TASK_SUCCESS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE_TASK_FAILURE', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=927,
  serialized_end=1192,
)
_sym_db.RegisterEnumDescriptor(_ACK)

Ack = enum_type_wrapper.EnumTypeWrapper(_ACK)
_TASKSTATUS = _descriptor.EnumDescriptor(
  name='TaskStatus',
  full_name='com.nextsmarty.nstm.rpc.TaskStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE_FAIL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE_SUCCESS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1194,
  serialized_end=1252,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATUS)

TaskStatus = enum_type_wrapper.EnumTypeWrapper(_TASKSTATUS)
SUBMIT_SUCCESS = 0
SUBMIT_FAILURE_EXISTS = 1
DELETE_SUCCESS = 2
DELETE_FAILURE_TASK_NOT_EXISTS = 3
NOT_DEFINE = 4
REGISTER_SUCCESS = 5
REGISTER_FAIL = 6
PULL_TASK_SUCCESS = 7
PULL_TASK_NO_TASK_SASTIFY = 8
DONE_TASK_SUCCESS = 9
DONE_TASK_FAILURE = 10
RUNNING = 0
DONE_FAIL = 1
DONE_SUCCESS = 2



_TASKDESCR = _descriptor.Descriptor(
  name='TaskDescr',
  full_name='com.nextsmarty.nstm.rpc.TaskDescr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskName', full_name='com.nextsmarty.nstm.rpc.TaskDescr.taskName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remoteUri', full_name='com.nextsmarty.nstm.rpc.TaskDescr.remoteUri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=91,
)


_DONETASKREQUEST = _descriptor.Descriptor(
  name='DoneTaskRequest',
  full_name='com.nextsmarty.nstm.rpc.DoneTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskName', full_name='com.nextsmarty.nstm.rpc.DoneTaskRequest.taskName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='com.nextsmarty.nstm.rpc.DoneTaskRequest.isSuccess', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=93,
  serialized_end=147,
)


_DONETASKRESPONE = _descriptor.Descriptor(
  name='DoneTaskRespone',
  full_name='com.nextsmarty.nstm.rpc.DoneTaskRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.nextsmarty.nstm.rpc.DoneTaskRespone.ack', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=149,
  serialized_end=209,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='com.nextsmarty.nstm.rpc.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskName', full_name='com.nextsmarty.nstm.rpc.DeleteRequest.taskName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=211,
  serialized_end=244,
)


_DELETETASKRESPONE = _descriptor.Descriptor(
  name='DeleteTaskRespone',
  full_name='com.nextsmarty.nstm.rpc.DeleteTaskRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.nextsmarty.nstm.rpc.DeleteTaskRespone.ack', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=246,
  serialized_end=308,
)


_SUBMITTASKREQUEST = _descriptor.Descriptor(
  name='SubmitTaskRequest',
  full_name='com.nextsmarty.nstm.rpc.SubmitTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskDescr', full_name='com.nextsmarty.nstm.rpc.SubmitTaskRequest.taskDescr', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=310,
  serialized_end=384,
)


_SUBMITTASKRESPONE = _descriptor.Descriptor(
  name='SubmitTaskRespone',
  full_name='com.nextsmarty.nstm.rpc.SubmitTaskRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.nextsmarty.nstm.rpc.SubmitTaskRespone.ack', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=386,
  serialized_end=448,
)


_PULLTASKREQUEST = _descriptor.Descriptor(
  name='PullTaskRequest',
  full_name='com.nextsmarty.nstm.rpc.PullTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='com.nextsmarty.nstm.rpc.PullTaskRequest.metrics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workerId', full_name='com.nextsmarty.nstm.rpc.PullTaskRequest.workerId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=450,
  serialized_end=546,
)


_PULLTASKRESPONE = _descriptor.Descriptor(
  name='PullTaskRespone',
  full_name='com.nextsmarty.nstm.rpc.PullTaskRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskDescr', full_name='com.nextsmarty.nstm.rpc.PullTaskRespone.taskDescr', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.nextsmarty.nstm.rpc.PullTaskRespone.ack', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=548,
  serialized_end=663,
)


_AVAILABLERESOURCE = _descriptor.Descriptor(
  name='AvailableResource',
  full_name='com.nextsmarty.nstm.rpc.AvailableResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpu', full_name='com.nextsmarty.nstm.rpc.AvailableResource.gpu', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=665,
  serialized_end=697,
)


_WORKERDESC = _descriptor.Descriptor(
  name='WorkerDesc',
  full_name='com.nextsmarty.nstm.rpc.WorkerDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='com.nextsmarty.nstm.rpc.WorkerDesc.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='com.nextsmarty.nstm.rpc.WorkerDesc.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu', full_name='com.nextsmarty.nstm.rpc.WorkerDesc.gpu', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpuInfo', full_name='com.nextsmarty.nstm.rpc.WorkerDesc.cpuInfo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=699,
  serialized_end=769,
)


_MASTERDESC = _descriptor.Descriptor(
  name='MasterDesc',
  full_name='com.nextsmarty.nstm.rpc.MasterDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='com.nextsmarty.nstm.rpc.MasterDesc.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpcPort', full_name='com.nextsmarty.nstm.rpc.MasterDesc.grpcPort', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=771,
  serialized_end=813,
)


_WORKERREGISTERREQUEST = _descriptor.Descriptor(
  name='WorkerRegisterRequest',
  full_name='com.nextsmarty.nstm.rpc.WorkerRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workerId', full_name='com.nextsmarty.nstm.rpc.WorkerRegisterRequest.workerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=815,
  serialized_end=856,
)


_WORKERREGISTERRESPONE = _descriptor.Descriptor(
  name='WorkerRegisterRespone',
  full_name='com.nextsmarty.nstm.rpc.WorkerRegisterRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.nextsmarty.nstm.rpc.WorkerRegisterRespone.ack', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=858,
  serialized_end=924,
)

_DONETASKRESPONE.fields_by_name['ack'].enum_type = _ACK
_DELETETASKRESPONE.fields_by_name['ack'].enum_type = _ACK
_SUBMITTASKREQUEST.fields_by_name['taskDescr'].message_type = _TASKDESCR
_SUBMITTASKRESPONE.fields_by_name['ack'].enum_type = _ACK
_PULLTASKREQUEST.fields_by_name['metrics'].message_type = _AVAILABLERESOURCE
_PULLTASKRESPONE.fields_by_name['taskDescr'].message_type = _TASKDESCR
_PULLTASKRESPONE.fields_by_name['ack'].enum_type = _ACK
_WORKERREGISTERRESPONE.fields_by_name['ack'].enum_type = _ACK
DESCRIPTOR.message_types_by_name['TaskDescr'] = _TASKDESCR
DESCRIPTOR.message_types_by_name['DoneTaskRequest'] = _DONETASKREQUEST
DESCRIPTOR.message_types_by_name['DoneTaskRespone'] = _DONETASKRESPONE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteTaskRespone'] = _DELETETASKRESPONE
DESCRIPTOR.message_types_by_name['SubmitTaskRequest'] = _SUBMITTASKREQUEST
DESCRIPTOR.message_types_by_name['SubmitTaskRespone'] = _SUBMITTASKRESPONE
DESCRIPTOR.message_types_by_name['PullTaskRequest'] = _PULLTASKREQUEST
DESCRIPTOR.message_types_by_name['PullTaskRespone'] = _PULLTASKRESPONE
DESCRIPTOR.message_types_by_name['AvailableResource'] = _AVAILABLERESOURCE
DESCRIPTOR.message_types_by_name['WorkerDesc'] = _WORKERDESC
DESCRIPTOR.message_types_by_name['MasterDesc'] = _MASTERDESC
DESCRIPTOR.message_types_by_name['WorkerRegisterRequest'] = _WORKERREGISTERREQUEST
DESCRIPTOR.message_types_by_name['WorkerRegisterRespone'] = _WORKERREGISTERRESPONE
DESCRIPTOR.enum_types_by_name['Ack'] = _ACK
DESCRIPTOR.enum_types_by_name['TaskStatus'] = _TASKSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskDescr = _reflection.GeneratedProtocolMessageType('TaskDescr', (_message.Message,), dict(
  DESCRIPTOR = _TASKDESCR,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.TaskDescr)
  ))
_sym_db.RegisterMessage(TaskDescr)

DoneTaskRequest = _reflection.GeneratedProtocolMessageType('DoneTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _DONETASKREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.DoneTaskRequest)
  ))
_sym_db.RegisterMessage(DoneTaskRequest)

DoneTaskRespone = _reflection.GeneratedProtocolMessageType('DoneTaskRespone', (_message.Message,), dict(
  DESCRIPTOR = _DONETASKRESPONE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.DoneTaskRespone)
  ))
_sym_db.RegisterMessage(DoneTaskRespone)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteTaskRespone = _reflection.GeneratedProtocolMessageType('DeleteTaskRespone', (_message.Message,), dict(
  DESCRIPTOR = _DELETETASKRESPONE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.DeleteTaskRespone)
  ))
_sym_db.RegisterMessage(DeleteTaskRespone)

SubmitTaskRequest = _reflection.GeneratedProtocolMessageType('SubmitTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITTASKREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.SubmitTaskRequest)
  ))
_sym_db.RegisterMessage(SubmitTaskRequest)

SubmitTaskRespone = _reflection.GeneratedProtocolMessageType('SubmitTaskRespone', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITTASKRESPONE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.SubmitTaskRespone)
  ))
_sym_db.RegisterMessage(SubmitTaskRespone)

PullTaskRequest = _reflection.GeneratedProtocolMessageType('PullTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _PULLTASKREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.PullTaskRequest)
  ))
_sym_db.RegisterMessage(PullTaskRequest)

PullTaskRespone = _reflection.GeneratedProtocolMessageType('PullTaskRespone', (_message.Message,), dict(
  DESCRIPTOR = _PULLTASKRESPONE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.PullTaskRespone)
  ))
_sym_db.RegisterMessage(PullTaskRespone)

AvailableResource = _reflection.GeneratedProtocolMessageType('AvailableResource', (_message.Message,), dict(
  DESCRIPTOR = _AVAILABLERESOURCE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.AvailableResource)
  ))
_sym_db.RegisterMessage(AvailableResource)

WorkerDesc = _reflection.GeneratedProtocolMessageType('WorkerDesc', (_message.Message,), dict(
  DESCRIPTOR = _WORKERDESC,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.WorkerDesc)
  ))
_sym_db.RegisterMessage(WorkerDesc)

MasterDesc = _reflection.GeneratedProtocolMessageType('MasterDesc', (_message.Message,), dict(
  DESCRIPTOR = _MASTERDESC,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.MasterDesc)
  ))
_sym_db.RegisterMessage(MasterDesc)

WorkerRegisterRequest = _reflection.GeneratedProtocolMessageType('WorkerRegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _WORKERREGISTERREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.WorkerRegisterRequest)
  ))
_sym_db.RegisterMessage(WorkerRegisterRequest)

WorkerRegisterRespone = _reflection.GeneratedProtocolMessageType('WorkerRegisterRespone', (_message.Message,), dict(
  DESCRIPTOR = _WORKERREGISTERRESPONE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:com.nextsmarty.nstm.rpc.WorkerRegisterRespone)
  ))
_sym_db.RegisterMessage(WorkerRegisterRespone)


DESCRIPTOR._options = None

_NSTM = _descriptor.ServiceDescriptor(
  name='Nstm',
  full_name='com.nextsmarty.nstm.rpc.Nstm',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1255,
  serialized_end=1771,
  methods=[
  _descriptor.MethodDescriptor(
    name='PullTask',
    full_name='com.nextsmarty.nstm.rpc.Nstm.PullTask',
    index=0,
    containing_service=None,
    input_type=_PULLTASKREQUEST,
    output_type=_PULLTASKRESPONE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DoneTask',
    full_name='com.nextsmarty.nstm.rpc.Nstm.DoneTask',
    index=1,
    containing_service=None,
    input_type=_DONETASKREQUEST,
    output_type=_DONETASKRESPONE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='com.nextsmarty.nstm.rpc.Nstm.Register',
    index=2,
    containing_service=None,
    input_type=_WORKERREGISTERREQUEST,
    output_type=_WORKERREGISTERRESPONE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitTask',
    full_name='com.nextsmarty.nstm.rpc.Nstm.SubmitTask',
    index=3,
    containing_service=None,
    input_type=_SUBMITTASKREQUEST,
    output_type=_SUBMITTASKRESPONE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTask',
    full_name='com.nextsmarty.nstm.rpc.Nstm.DeleteTask',
    index=4,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETETASKRESPONE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NSTM)

DESCRIPTOR.services_by_name['Nstm'] = _NSTM

# @@protoc_insertion_point(module_scope)