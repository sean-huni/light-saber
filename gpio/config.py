import RPi.GPIO as GPIO

from command.voice import VoiceCmd

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
        VoiceCmd('System Shutdown Sequence in execution...', 'command/sp/speech_system-shutdown.mp3')
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
        VoiceCmd('Swimming Pool Flood-Light-1: ON', 'command/sp/speech_sp-fl-1-on.mp3')

    @staticmethod
    def bulb_off():
        GPIO.output(lBulb, GPIO.HIGH)
        VoiceCmd('Swimming Pool Flood-Light-1: OFF', 'command/sp/speech_sp-fl-1-off.mp3')

    """
    RED-LED-LIGHT
    """

    @staticmethod
    def led_red_onn():
        GPIO.output(ledRed, GPIO.LOW)
        VoiceCmd('Backyard Flood-Light-1: ON', 'command/sp/speech_by-fl-1-on.mp3')

    @staticmethod
    def led_red_off():
        GPIO.output(ledRed, GPIO.HIGH)
        VoiceCmd('Backyard Flood-Light-1: OFF', 'command/sp/speech_by-fl-1-off.mp3')

    """
    GREEN-LED-LIGHT
    """

    @staticmethod
    def led_green_onn():
        GPIO.output(ledGreen, GPIO.LOW)
        VoiceCmd('Backyard Flood-Light-2: ON', 'command/sp/speech_by-fl-2-on.mp3')

    @staticmethod
    def led_green_off():
        GPIO.output(ledGreen, GPIO.HIGH)
        VoiceCmd('Backyard Flood-Light-2: OFF', 'command/sp/speech_by-fl-2-off.mp3')

    """
    BLUE-LED-LIGHT
    """

    @staticmethod
    def led_blue_onn():
        GPIO.output(ledBlue, GPIO.LOW)
        VoiceCmd('Swimming Pool Flood-Light-2: ON', 'command/sp/speech_sp-fl-2-on.mp3')

    @staticmethod
    def led_blue_off():
        GPIO.output(ledBlue, GPIO.HIGH)
        VoiceCmd('Swimming Pool Flood-Light-2: OFF', 'command/sp/speech_sp-fl-2-off.mp3')

    @staticmethod
    def all_lights_off():
        GPIO.output(ledBlue, GPIO.HIGH)
        GPIO.output(ledGreen, GPIO.HIGH)
        GPIO.output(ledRed, GPIO.HIGH)
        GPIO.output(lBulb, GPIO.HIGH)
        VoiceCmd('All Flood Lights: OFF', 'command/sp/speech_all-fl-off.mp3')

    @staticmethod
    def all_lights_on():
        GPIO.output(ledBlue, GPIO.LOW)
        GPIO.output(ledGreen, GPIO.LOW)
        GPIO.output(ledRed, GPIO.LOW)
        GPIO.output(lBulb, GPIO.LOW)
        VoiceCmd('All Flood Lights: ON', 'command/sp/speech_all-fl-on.mp3')
