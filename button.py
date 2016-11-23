#--------------------------------------
# Basic button read
#--------------------------------------
import time

import RPi.GPIO as IO

BUTTON_PIN = 26
DEBOUNCE = 0.25

IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setup(BUTTON_PIN, IO.IN, pull_up_down=IO.PUD_DOWN)

print "This is the button program."

count = 0

while True:
    if IO.input(BUTTON_PIN):
        count = count + 1
        print count
        time.sleep(DEBOUNCE)