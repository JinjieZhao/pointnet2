from functools import partial
import numpy as np

from flask import Flask
from flask_restful import request
from flask_restful import Resource, Api

import evaluate_part

app = Flask(__name__)
api = Api(app=app)

s, o = evaluate_part.evaluate()
eval_one = partial(evaluate_part.eval_one, s, o)
print("--**-- server initialized --**--")


class PointNet(Resource):

    def get(self):
        data = request.json['ndarray']
        array = np.array(data)

        return {'ndarray': eval_one(array).tolist()}


api.add_resource(PointNet, '/point')

if __name__ == '__main__':
    app.run()
