from __future__ import print_function

import time

import os
import numpy as np
import grpc

import pointnet2_pb2_grpc
import converter
import part_dataset_all_normal

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'shapenetcore_partanno_segmentation_benchmark_v0_normal')
TEST_DATASET = part_dataset_all_normal.PartNormalDataset(root=DATA_PATH, npoints=2048, classification=False,
                                                         split='test')


def get_data(num):
    for data in (TEST_DATASET.get_data(i) for i in np.random.choice(1000, num)):
        request = converter.ndarray_to_point_request(data)
        yield request


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pointnet2_pb2_grpc.PointStub(channel)
        cnt = 100

        start = time.time()
        replies = stub.Segment(get_data(cnt))
        for reply in replies:
            data = converter.point_reply_to_ndarray(reply)
        end = time.time()
        print(end - start, 's')


if __name__ == '__main__':
    run()
