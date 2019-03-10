from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import RPi.GPIO as GPIO

app = Flask(__name__)
api = Api(app)

lBulb = 22  # GPIO.BOARD=22 OR GPIO.BCM=25


class Config:

    @staticmethod
    def config():
        print('GPIO.BOARD.lBulb: ' + str(lBulb))
        GPIO.setmode(GPIO.BOARD)  # Pin-Numbers by Broadcom SOC Channel
        GPIO.setup(lBulb, GPIO.OUT)  # Relay Module Channel 1
        GPIO.output(lBulb, GPIO.HIGH)  # Turn off Chanel 1

    @staticmethod
    def clear_up():
        GPIO.output(lBulb, GPIO.LOW)  # GREEN LED-OFF
        GPIO.cleanup()  # Release Hardware Resources

    @staticmethod
    def onn():
        GPIO.output(lBulb, GPIO.LOW)
        print("Light-Turned: ONN")

    @staticmethod
    def off():
        GPIO.output(lBulb, GPIO.HIGH)
        print("Light-Turned: OFF")


class ToggleSwitch(Resource):
    def put(self, device):
        switch = request.json['switch']
        resp = {'data': 'device-id: ' + device, 'switch': switch}

        print(resp)

        if device == '1':
            if switch == 'ONN':
                Config.onn()
            else:
                Config.off()
        else:
            print('No device found...')

        resp = {'response': 'successful', 'code': 200}
        return jsonify(resp)


api.add_resource(ToggleSwitch, '/api/v1/device/<device>')  # Route_1

if __name__ == '__main__':
    try:
        Config.config()
        app.debug = True
        app.run(host='0.0.0.0', port='8083')
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
        print(" Oh Noo, looks like our fun has been cut-short!!!")
        Config.clear_up()

