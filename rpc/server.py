from __future__ import print_function
import pointnet2_pb2_grpc
import converter
from concurrent import futures
import grpc


class Server(pointnet2_pb2_grpc.PointServicer):
    def __init__(self):
        pass

    def Segment(self, request_iterator, context):
        for request in request_iterator:
            data = converter.point_request_to_ndarray(request)
            reply_data = data[:, -1]
            reply = converter.ndarray_to_point_reply(reply_data)
            yield reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pointnet2_pb2_grpc.add_PointServicer_to_server(
        Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
