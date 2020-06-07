from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import RPi.GPIO as GPIO
import datetime as dt
from json import dumps
from voice import Voice 

app = Flask(__name__)
api = Api(app)

lBulb = 22  # GPIO.BOARD=22 OR GPIO.BCM=25  >>> GPIO 25
ledRed = 11  # GPIO 17
ledGreen = 13  # GPIO 27
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
        VoiceCmd('System Shutdown Sequence in execution...', 'voice-feedback/speech_system-shutdown.mp3')
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
        VoiceCmd('Swimming Pool Flood-Light-1: ON', 'voice-feedback/speech_sp-fl-1-on.mp3')

    @staticmethod
    def bulb_off():
        GPIO.output(lBulb, GPIO.HIGH)
        VoiceCmd('Swimming Pool Flood-Light-1: OFF', 'voice-feedback/speech_sp-fl-1-off.mp3')

    """
    RED-LED-LIGHT
    """
    @staticmethod
    def led_red_onn():
        GPIO.output(ledRed, GPIO.LOW)
        VoiceCmd('Backyard Flood-Light-1: ON', 'voice-feedback/speech_by-fl-1-on.mp3')

    @staticmethod
    def led_red_off():
        GPIO.output(ledRed, GPIO.HIGH)
        VoiceCmd('Backyard Flood-Light-1: OFF', 'voice-feedback/speech_by-fl-1-off.mp3')

    """
    GREEN-LED-LIGHT
    """
    @staticmethod
    def led_green_onn():
        GPIO.output(ledGreen, GPIO.LOW)
        VoiceCmd('Backyard Flood-Light-2: ON', 'voice-feedback/speech_by-fl-2-on.mp3')

    @staticmethod
    def led_green_off():
        GPIO.output(ledGreen, GPIO.HIGH)
        VoiceCmd('Backyard Flood-Light-2: OFF', 'voice-feedback/speech_by-fl-2-off.mp3')

    """
    BLUE-LED-LIGHT
    """
    @staticmethod
    def led_blue_onn():
        GPIO.output(ledBlue, GPIO.LOW)
        VoiceCmd('Swimming Pool Flood-Light-2: ON', 'voice-feedback/speech_sp-fl-2-on.mp3')


    @staticmethod
    def led_blue_off():
        GPIO.output(ledBlue, GPIO.HIGH)
        VoiceCmd('Swimming Pool Flood-Light-2: OFF', 'voice-feedback/speech_sp-fl-2-off.mp3')

    @staticmethod
    def all_lights_off():
        GPIO.output(ledBlue, GPIO.HIGH)
        GPIO.output(ledGreen, GPIO.HIGH)
        GPIO.output(ledRed, GPIO.HIGH)
        GPIO.output(lBulb, GPIO.HIGH)
        VoiceCmd('All Flood Lights: OFF', 'voice-feedback/speech_all-fl-off.mp3')

    @staticmethod
    def all_lights_on():
        GPIO.output(ledBlue, GPIO.LOW)
        GPIO.output(ledGreen, GPIO.LOW)
        GPIO.output(ledRed, GPIO.LOW)
        GPIO.output(lBulb, GPIO.LOW)
        VoiceCmd('All Flood Lights: ON', 'voice-feedback/speech_all-fl-on.mp3')


class ToggleSwitch(Resource):
    def put(self, device):
        print(request.json)
        switch = request.json['switch']
        req = {'data': 'device-id: ' + device, 'switch': switch}

        print(req)

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
        elif device == '101':
             if switch == 'ONN':
                Config.all_lights_on()
             else:
                Config.all_lights_off()
        else:
            print('No device found...')

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


class VoiceCmd:
   def __init__(self, msg, filename):
       print(msg)
       init = Voice(filename)
       init.play()


api.add_resource(HealthCheck, '/api/v1/host')  # Route_1
api.add_resource(ToggleSwitch, '/api/v1/devices/<device>')  # Route_2

if __name__ == '__main__':
    try:
        VoiceCmd('System Startup sequence in execution', 'voice-feedback/speech_system-startup.mp3')
        Config.config()
        VoiceCmd('System Initialisation Completed!!!', 'voice-feedback/speech_system-init-complete.mp3')
        app.debug = True
        app.run(host='0.0.0.0', port='8083')
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be executed.
        print("Oh Noo, looks like our fun has been cut-short!!!")
        Config.clear_up()

