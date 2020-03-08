import numpy as np

from flask import Flask
from flask_restful import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app=app)


class PointNet(Resource):

    def get(self):
        data = request.json['ndarray']
        print(np.array(data).shape)

        return {'ndarray': np.random.rand(1, 2048, 1).tolist()}


api.add_resource(PointNet, '/point')

if __name__ == '__main__':
    app.run(debug=True)
