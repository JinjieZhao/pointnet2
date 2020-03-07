from io import BytesIO
import numpy as np

from pointnet2_pb2 import PointRequest, PointReply


def point_request_to_ndarray(PointRequest):
    bs = BytesIO(PointRequest.ndarray)
    return np.load(bs)


def point_reply_to_ndarray(PointReply):
    bs = BytesIO(PointReply.ndarray)
    return np.load(bs)


def ndarray_to_point_request(ndarray):
    bs = BytesIO()
    np.save(bs, ndarray)
    return PointRequest(ndarray=bs.getvalue())


def ndarray_to_point_reply(ndarray):
    bs = BytesIO()
    np.save(bs, ndarray)
    return PointReply(ndarray=bs.getvalue())


if __name__ == '__main__':
    # simple test
    label = np.random.random((1, 2048))
    reply = ndarray_to_point_reply(label)
    label_back = point_reply_to_ndarray(reply)
    assert np.array_equal(label, label_back)

    data = np.random.random((1, 2048, 7))
    request = ndarray_to_point_request(data)
    data_back = point_request_to_ndarray(request)
    assert np.array_equal(data, data_back)
