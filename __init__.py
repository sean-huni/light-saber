from command.voice import VoiceCmd
from commons.utility import Utility
from gpio.flood_lights import FloodLights
from rest.switch import api, HealthCheck, ToggleSwitch


class Main:
    def __init__(self):
        print('{0}: Main-instance Instantiated successfully!!!'.format(self.getStrDate()))

    def getStrDate(self) -> str:
        resp = Utility.getStrDate()
        return resp


if __name__ == '__main__':
    main = Main()
    try:
        VoiceCmd('{0}: System Startup sequence in execution'.format(str(main.getStrDate())), 'command/sp/speech_system-startup.mp3')
        FloodLights.config()
        api.add_resource(HealthCheck, '/api/v1/host')  # Route_1
        api.add_resource(ToggleSwitch, '/api/v1/devices/<device>')  # Route_2
        api.app.debug = True
        VoiceCmd('{0}: System Initialisation Completed!!!'.format(str(main.getStrDate())), 'command/sp/speech_system-init-complete.mp3')
        api.app.run(host='0.0.0.0', port='8083')
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be executed.
        print('{0}: Graceful Termination'.format(str(main.getStrDate())))
    except Exception:
        print('{0}: System Error'.format(str(main.getStrDate())))
    finally:
        print('{0}: GPIO Cleanup'.format(str(main.getStrDate())))
        FloodLights.clear_up()
        print('{0}: System shutdown'.format(str(main.getStrDate())))
