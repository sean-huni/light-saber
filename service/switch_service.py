from gpio.flood_lights import FloodLights


class SwitchService:
    def toggle(self, device, switch):

        if device == '1':
            if switch == 'ONN':
                FloodLights.bulb_onn()
            else:
                FloodLights.bulb_off()
        elif device == '2':
            if switch == 'ONN':
                FloodLights.led_red_onn()
            else:
                FloodLights.led_red_off()
        elif device == '3':
            if switch == 'ONN':
                FloodLights.led_green_onn()
            else:
                FloodLights.led_green_off()
        elif device == '4':
            if switch == 'ONN':
                FloodLights.led_blue_onn()
            else:
                FloodLights.led_blue_off()
        elif device == '101':
            if switch == 'ONN':
                FloodLights.all_lights_on()
            else:
                FloodLights.all_lights_off()
        else:
            print('No device found...')
