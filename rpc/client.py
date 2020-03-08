from __future__ import print_function

import time

import grpc

import pointnet2_pb2_grpc
import converter
import part_dataset_all_normal


def get_data(dataset):
    for data in dataset:
        request = converter.ndarray_to_point_request(data)
        yield request


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pointnet2_pb2_grpc.PointStub(channel)
        cnt = 100
        dataset = part_dataset_all_normal.list_data(cnt)

        data_list = get_data(dataset)
        start = time.time()
        for reply in stub.Segment(data_list):
            data = converter.point_reply_to_ndarray(reply)
        end = time.time()
        print(end - start, 's')


if __name__ == '__main__':
    run()
