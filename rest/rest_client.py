import json
import requests
import numpy as np


def segment():
    url = "http://127.0.0.1:5000/point"

    files = {'ndarray': np.random.rand(1, 2048, 7).tolist()}

    response = requests.request("GET", url, json=files)

    json_array = json.loads(response.text)['ndarray']
    print(np.array(json_array).shape)


if __name__ == '__main__':
    segment()
