import RPi.GPIO as GPIO
import time

lBulb = 22  # GPIO.BOARD=22 OR GPIO.BCM=25

# Timers
lbTimerONN = 3.5
lbTimerOFF = 0.5

txtOnIdle = "System Idle..."
txtBulbONN = "Light-Bulb ONN..."
txtBulbOFF = "Light-Bulb OFF..."

GPIO.setmode(GPIO.BOARD)  # Pin-Numbers by Broadcom SOC Channel


# Setting up/initiasing program parameters
def init():
    # Light & Motion Sensor Setup
    GPIO.setup(lBulb, GPIO.OUT)  # Relay Module Channel 1

    GPIO.output(lBulb, GPIO.LOW)  # Turn off Chanel 1


# Function Definition for cleaning-up environment.
def clear_up():
    GPIO.output(lBulb, GPIO.LOW)  # GREEN LED-OFF
    GPIO.cleanup()  # Release Hardware Resources


# Turn onn the Red-Led to indicate motion detection.
# Simultaneously turn off the Green-Led as the Light Bulb Turns ONN.
def on_motion():
    print(txtBulbONN)
    GPIO.output(lBulb, GPIO.LOW)


# Waiting for an event to occur on the Motion-Sensor
def on_idle():
    print(txtBulbOFF)
    GPIO.output(lBulb, GPIO.HIGH)
    print(txtOnIdle)


def prg_loop():
    i = 1
    while True:
        # Counter Feedback
        print("Cycle: " + str(i))
        on_idle()
        time.sleep(lbTimerOFF)
        on_motion()
        time.sleep(lbTimerONN)
        i += 1  # Increment counter by 1


# Program execution begins here...
if __name__ == '__main__':
    print('Press Ctrl-C to terminate program...')
    print('Initialising...')
    init()
    print('Initialisation complete!!!')

    try:
        prg_loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
        print(" Oh Noo, looks like our fun has been cut-short!!!")
        clear_up()

