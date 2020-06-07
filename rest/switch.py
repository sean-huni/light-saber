import datetime as dt
from json import dumps

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from service.switch_service import SwitchService

app = Flask(__name__)
api = Api(app)

switchService = SwitchService

class ToggleSwitch(Resource):
    def put(self, device):
        print(request.json)
        switch = request.json['switch']
        req = {'data': 'device-id: ' + device, 'switch': switch}

        switchService.toggle(device, switch)
        print('{0}: Request: {1}'.format(StrMsg.getStrDate(), req))

        resp = {'response': 'successful', 'code': 200}
        print('{0}: {1}'.format(StrMsg.getStrDate(), resp))
        return jsonify(resp)


class HealthCheck(Resource):
    def get(self):
        name = 'RPi-1'
        deviceType = 'HOST_DEVICE'
        status = 'ONLINE'
        lDateTime = dumps(dt.datetime.now(), indent=4, sort_keys=True, default=str)
        resp = {'name': str(name), 'deviceType': deviceType, 'eStatus': status, 'lDateTime': str(lDateTime).strip('"')}
        print('{0}: Response: {1}'.format(StrMsg.getStrDate(), resp))
        return jsonify(resp)


class StrMsg:
    @staticmethod
    def getStrDate(self) -> str:
        lDateTime = dumps(dt.datetime.now(), indent=4, sort_keys=True, default=str)
        resp = str(lDateTime).strip('"')
        return resp