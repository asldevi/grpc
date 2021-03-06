# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import math_pb2 as math__pb2


class CalculatorStub(object):
  """The calc service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoMath = channel.unary_unary(
        '/math.Calculator/DoMath',
        request_serializer=math__pb2.MathRequest.SerializeToString,
        response_deserializer=math__pb2.MathReply.FromString,
        )


class CalculatorServicer(object):
  """The calc service definition.
  """

  def DoMath(self, request, context):
    """does the math
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoMath': grpc.unary_unary_rpc_method_handler(
          servicer.DoMath,
          request_deserializer=math__pb2.MathRequest.FromString,
          response_serializer=math__pb2.MathReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'math.Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
