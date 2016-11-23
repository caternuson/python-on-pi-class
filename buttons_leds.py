#--------------------------------------
# Buttons + LEDs
#--------------------------------------
import time

import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)

BUTTONS = [26, 19, 13]
LEDS =    [22, 27, 17]

for PIN in LEDS:
    IO.setup(PIN, IO.OUT)
    IO.output(PIN, IO.LOW)
    
for PIN in BUTTONS:
    IO.setup(PIN, IO.IN, pull_up_down=IO.PUD_DOWN)
    
while True:
    for i in xrange(len(BUTTONS)):
        if IO.input(BUTTONS[i]):
            IO.output(LEDS[i], IO.HIGH)
        else:
            IO.output(LEDS[i], IO.LOW)