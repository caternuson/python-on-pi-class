#--------------------------------------
# Button + LED
#--------------------------------------
import time

import RPi.GPIO as IO

BUTTON_PIN = 26
LED_PIN = 22
DEBOUNCE = 0.25

IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setup(LED_PIN, IO.OUT)
IO.setup(BUTTON_PIN, IO.IN, pull_up_down=IO.PUD_DOWN)

print "This is the button and LED program."

while True:
    if IO.input(BUTTON_PIN):
        IO.output(LED_PIN, IO.HIGH)
        time.sleep(DEBOUNCE)
    else:
        IO.output(LED_PIN, IO.LOW)