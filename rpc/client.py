from __future__ import print_function

import time

import grpc

import pointnet2_pb2_grpc
import converter
import part_dataset_all_normal

cnt = 100

dataset = part_dataset_all_normal.list_data(cnt)


def get_data(dataset):
    for data in dataset:
        request = converter.ndarray_to_point_request(data)
        yield request


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = pointnet2_pb2_grpc.PointStub(channel)

        start = time.time()
        for reply in stub.Segment(get_data(dataset)):
            data = converter.point_reply_to_ndarray(reply)
        end = time.time()
        print(end - start, 's')


if __name__ == '__main__':
    for _ in range(3):
        run()
