import datetime as dt
from json import dumps

from command.voice import VoiceCmd
from gpio.config import Config
from rest.switch import api


class Main:
    def __init__(self):
        print('{0}: Main-instance Instantiated successfully!!!'.self.getStrDate())

    def getStrDate(self) -> str:
        lDateTime = dumps(dt.datetime.now(), indent=4, sort_keys=True, default=str)
        resp = str(lDateTime).strip('"')
        return resp


if __name__ == '__main__':
    main = Main()
    try:
        VoiceCmd('{0}: System Startup sequence in execution'.format(str(main.getStrDate())),
                 'command/sp/speech_system-startup.mp3')
        Config.config()
        api.app.debug = True
        VoiceCmd('{0}: System Initialisation Completed!!!'.format('command/sp/speech_system-init-complete.mp3'))
        api.app.run(host='0.0.0.0', port='8083')
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be executed.
        print('{0}: Oh Noo, looks like our fun has been cut-short!!!'.format(str(main.getStrDate())))
        Config.clear_up()
