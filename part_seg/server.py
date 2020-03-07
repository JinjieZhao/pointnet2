from __future__ import print_function

from concurrent import futures
from functools import partial
import grpc

import evaluate_part
import pointnet2_pb2_grpc
import converter


class Server(pointnet2_pb2_grpc.PointServicer):
    def __init__(self):
        s, o = evaluate_part.evaluate()
        self.eval_one = partial(evaluate_part.eval_one, s, o)

    def Segment(self, request_iterator, context):
        for request in request_iterator:
            data = converter.point_request_to_ndarray(request)
            reply_data = self.eval_one(data)
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
