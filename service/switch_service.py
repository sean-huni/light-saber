from gpio.flood_lights import FloodLights
from gpio.lcd_display import LcdDevice


class SwitchService:
    lcd = LcdDevice()

    def __init__(self):
        self.lcd.x = False

    def toggle(self, device, switch):

        if device == '1':
            if switch == 'ONN':
                FloodLights.bulb_onn()
                self.lcd.display_msg('Swimming-PL FL-1\nSwitch: ON')
            else:
                FloodLights.bulb_off()
                self.lcd.display_msg('Swimming-PL FL-1\nSwitch: OFF')
        elif device == '2':
            if switch == 'ONN':
                FloodLights.led_red_onn()
                self.lcd.display_msg('Backyard FL-1\nSwitch: ON')
            else:
                FloodLights.led_red_off()
                self.lcd.display_msg('Backyard FL-1\nSwitch: OFF')
        elif device == '3':
            if switch == 'ONN':
                FloodLights.led_green_onn()
                self.lcd.display_msg('Backyard FL-2\nSwitch: ON')
            else:
                FloodLights.led_green_off()
                self.lcd.display_msg('Backyard FL-2\nSwitch: OFF')
        elif device == '4':
            if switch == 'ONN':
                FloodLights.led_blue_onn()
                self.lcd.display_msg('Swimming-PL FL-2\nSwitch: ON')
            else:
                FloodLights.led_blue_off()
                self.lcd.display_msg('Swimming-PL FL-2\nSwitch: OFF')
        elif device == '101':
            if switch == 'ONN':
                FloodLights.all_lights_on()
                self.lcd.display_msg('All Flood Lights\nSwitch: ON')
            else:
                FloodLights.all_lights_off()
                self.lcd.display_msg('All Flood Lights\nSwitch: OFF')
        else:
            print('No device found...')
