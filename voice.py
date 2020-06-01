from pydub import AudioSegment
from pydub.playback import play

class Voice:
     def __init__(self, filename):
         print('filename: ' + str(filename))
         self.vc_cmd = AudioSegment.from_mp3(filename)

     def play(self):
         play(self.vc_cmd)
