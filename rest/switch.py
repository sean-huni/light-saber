import datetime as dt
from json import dumps

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ToggleSwitch(Resource):
    def put(self, device):
        print(request.json)
        switch = request.json['switch']
        req = {'data': 'device-id: ' + device, 'switch': switch}

        print(req)

        resp = {'response': 'successful', 'code': 200}
        return jsonify(resp)


class HealthCheck(Resource):
    def get(self):
        name = 'RPi-1'
        deviceType = 'HOST_DEVICE'
        status = 'ONLINE'
        lDateTime = dumps(dt.datetime.now(), indent=4, sort_keys=True, default=str)
        resp = {'name': str(name), 'deviceType': deviceType, 'eStatus': status, 'lDateTime': str(lDateTime).strip('"')}
        print(resp)
        return jsonify(resp)


api.add_resource(HealthCheck, '/api/v1/host')  # Route_1
api.add_resource(ToggleSwitch, '/api/v1/devices/<device>')  # Route_2
