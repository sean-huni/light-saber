from gpio.config import Config


class SwitchService:
    def toggle(self, device, switch):

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
