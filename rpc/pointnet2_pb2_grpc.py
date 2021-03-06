# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pointnet2_pb2 as pointnet2__pb2


class PointStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Segment = channel.stream_stream(
        '/pointnet2.Point/Segment',
        request_serializer=pointnet2__pb2.PointRequest.SerializeToString,
        response_deserializer=pointnet2__pb2.PointReply.FromString,
        )


class PointServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Segment(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PointServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Segment': grpc.stream_stream_rpc_method_handler(
          servicer.Segment,
          request_deserializer=pointnet2__pb2.PointRequest.FromString,
          response_serializer=pointnet2__pb2.PointReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pointnet2.Point', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
