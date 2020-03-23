import json
import time
import requests
import numpy as np

import part_dataset_all_normal

cnt = 100
dataset = part_dataset_all_normal.list_data(cnt)


def segment():
    url = "http://127.0.0.1:5001/point"
    s = requests.Session()

    start = time.time()
    for data in dataset:
        files = {'ndarray': data.tolist()}

        response = s.request("GET", url, json=files)

        json_array = json.loads(response.text)['ndarray']
        array = np.array(json_array)
    end = time.time()

    print end - start


if __name__ == '__main__':
    for _ in range(3):
        segment()
