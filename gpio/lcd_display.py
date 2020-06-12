# -*- coding: utf-8 -*-

import re
import subprocess
import sys
import time
from multiprocessing import *

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
    proc_count = 0
    p = None
    lcd = None
    processes = []

    def __init__(self):
        if self.lcd is None:
            # Initialize the LCD using the pins above.
            self.lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
            print('{0}: LCD Instance Created!!!'.format(Utility.getStrDate()))

    def display_msg(self, msg):
        self.kill_live_processes()

        # Print a message
        self.lcd.clear()
        self.lcd.message(str(msg))
        time.sleep(3.0)

        # process.daemon = True
        self.p = Process(target=self.print_cpu_data, name='PROC-{0}'.format(self.proc_count))  # , args=(self,)
        self.p.start()
        self.processes.append(self.p)
        self.proc_count += 1
        print('{0}: is New-Thread Alive: {1}'.format(Utility.getStrDate(), self.p.is_alive()))

    # Async method that executes behind the scenes to print resource-temperatures :-)
    def print_cpu_data(self):
        while True:
            cpu = subprocess.getoutput('cat /sys/class/thermal/thermal_zone0/temp')
            gpu = subprocess.getoutput('/opt/vc/bin/vcgencmd measure_temp')
            cpu = re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+', cpu)
            gpu = re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+', gpu)
            cpu = float(cpu[0]) / 1000
            gpu = float(gpu[0])
            print('{0}: CPU: {1:.2f}{3}C\tGPU: {2:.2f}{3}C'.format(Utility.getStrDate(), cpu, gpu, '°'))
            self.lcd.clear()
            self.lcd.message('CPU: {0:.2f}{2}C\nGPU: {1:.2f}{2}C'.format(cpu, gpu, chr(223)))
            time.sleep(1.0)

    @staticmethod
    def kill_live_processes():
        print('{0}: Current-Active processes: {1}'.format(Utility.getStrDate(), LcdDevice.processes))

        for proc in LcdDevice.processes:
            proc.terminate()
            print('{0}: {1} isAlive: {2}'.format(Utility.getStrDate(), proc.name, proc.is_alive()))
            old_pro = LcdDevice.processes.pop(0)
            print('{0}: {1} Proc-Popped'.format(Utility.getStrDate(), old_pro.name))