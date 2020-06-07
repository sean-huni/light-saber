from commons.utility import Utility

lcd_pin3 = 25 #GPIO 25 >> pin 25
lcd_ping6 = 18  #GPIO 24 >> pin 18
lcd_ping11 = 16  #GPIO 23 >> pin 16
lcd_ping12 = 7  #GPIO 4 >> pin 7
lcd_ping13 = 31  #GPIO 6 >> pin 31
lcd_ping14 = 33  #GPIO 6 >> pin 13

class LCD:
    def __init__(self):
        print('{0}: LCD Instance Created!!!'.format(Utility.getStrDate()))