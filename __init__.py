from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import RPi.GPIO as GPIO

app = Flask(__name__)
api = Api(app)

lBulb = 22  # GPIO.BOARD=22 OR GPIO.BCM=25  >>> GPIO 25
ledRed = 11  # GPIO 17
ledGreen = 13  # GPIO 15
ledBlue = 15  # GPIO 22


class Config:

    @staticmethod
    def config():
        print('GPIO.BOARD.lBulb: ' + str(lBulb))
        GPIO.setmode(GPIO.BOARD)  # Pin-Numbers by Broadcom SOC Channel
        GPIO.setup(lBulb, GPIO.OUT)  # Relay Module Channel 1
        GPIO.output(lBulb, GPIO.LOW)  # Turn off Channel 1

        print('GPIO.BOARD.LedRed: ' + str(ledRed))
        GPIO.setup(ledRed, GPIO.OUT)  # Relay Module Channel 2
        GPIO.output(ledRed, GPIO.LOW)  # Turn off Channel 2

        print('GPIO.BOARD.LedGreen: ' + str(ledGreen))
        GPIO.setup(ledGreen, GPIO.OUT)  # Relay Module Channel 3
        GPIO.output(ledGreen, GPIO.LOW)  # Turn off Channel 3

        print('GPIO.BOARD.LedBlue: ' + str(ledBlue))
        GPIO.setup(ledBlue, GPIO.OUT)  # Relay Module Channel 4
        GPIO.output(ledBlue, GPIO.LOW)  # Turn off Channel 4

    @staticmethod
    def clear_up():
        GPIO.output(lBulb, GPIO.LOW)  # Light-Bulb LED-OFF
        GPIO.output(ledRed, GPIO.LOW)  # RED LED-OFF
        GPIO.output(ledGreen, GPIO.LOW)  # GREEN LED-OFF
        GPIO.output(ledBlue, GPIO.LOW)  # BLUE LED-OFF
        GPIO.cleanup()  # Release Hardware Resources

    """
    NEON-LIGHT BULB
    """
    @staticmethod
    def bulb_onn():
        GPIO.output(lBulb, GPIO.LOW)
        print("Light-Turned: ONN")

    @staticmethod
    def bulb_off():
        GPIO.output(lBulb, GPIO.HIGH)
        print("Light-Turned: OFF")

    """
    RED-LED-LIGHT
    """
    @staticmethod
    def led_red_onn():
        GPIO.output(ledRed, GPIO.LOW)
        print("RED-LED-LIGHT: ONN")

    @staticmethod
    def led_red_off():
        GPIO.output(ledRed, GPIO.HIGH)
        print("RED-LED-LIGHT: OFF")

    """
    GREEN-LED-LIGHT
    """
    @staticmethod
    def led_green_onn():
        GPIO.output(ledGreen, GPIO.LOW)
        print("GREEN-LED-LIGHT: ONN")

    @staticmethod
    def led_green_off():
        GPIO.output(ledGreen, GPIO.HIGH)
        print("GREEN-LED-LIGHT: OFF")

    """
    BLUE-LED-LIGHT
    """
    @staticmethod
    def led_blue_onn():
        GPIO.output(ledBlue, GPIO.LOW)
        print("BLUE-LED-LIGHT: ONN")

    @staticmethod
    def led_blue_off():
        GPIO.output(ledBlue, GPIO.HIGH)
        print("BLUE-LED-LIGHT: OFF")


class ToggleSwitch(Resource):
    def put(self, device):
        switch = request.json['switch']
        resp = {'data': 'device-id: ' + device, 'switch': switch}

        print(resp)

        if device == '1':
            if switch == 'ONN':
                Config.bulb_onn()
            else:
                Config.bulb_off()
        elif device == '2':
            if switch == 'ONN':
                Config.led_red_onn()
            else:
                Config.led_red_off()
        elif device == '3':
            if switch == 'ONN':
                Config.led_green_onn()
            else:
                Config.led_green_off()
        elif device == '4':
            if switch == 'ONN':
                Config.led_blue_onn()
            else:
                Config.led_blue_off()
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
        print("Oh Noo, looks like our fun has been cut-short!!!")
        Config.clear_up()

api.add_resource(ToggleSwitch, '/api/v1/device/<device>')  # Route_1

