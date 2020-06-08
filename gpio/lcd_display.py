import sys
import time

import commands
from gpiozero import CPUTemperature

from commons.utility import Utility

sys.path.append('/home/pi/proj/python/pi/Adafruit_Python_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD as LCD

# Raspberry Pi GPIO configuration (NOT Pin Numbers):
lcd_rs = 5  # Pin 29 GPIO 05 >> prev 27  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en = 24  # Pin 18 GPIO 24 >> prev 22
lcd_d4 = 23  # Pin 16 GPIO 23 >> prev 25
lcd_d5 = 4  # Pin 07 GPIO 04 >> prev 24
lcd_d6 = 6  # Pin 31 GPIO 06 >> prev 23
lcd_d7 = 13  # Pin 33 GPIO 13 >> prev 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2


class LcdDevice:
    x = False
    lcd = None

    def __init__(self):
        # Initialize the LCD using the pins above.
        self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
        print('{0}: LCD Instance Created!!!'.format(Utility.getStrDate()))

    def display_msg(self, msg):
        # Print a message
        self.lcd.clear()
        self.lcd.message(str(msg))
        time.sleep(5.0)
        self.x = True
        self.print_cpu_data()

    # Async method that executes behind the scenes to print resource-temperatures :-)
    async def print_cpu_data(self):
        while self.x:
            cpu = CPUTemperature()
            gpu = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp')
            gpu = float(gpu)

            # lcd.clear()
            self.lcd.message('CPU: {0:.2f}°C\nGPU: {1:.2f}°C'.format(cpu, gpu))
            time.sleep(1.0)
