#--------------------------------------
# Basic LED blink
#--------------------------------------
import time

import RPi.GPIO as IO

LED_PIN = 27
DELAY = 0.2    # seconds

IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setup(LED_PIN, IO.OUT)

print "This is the blink program."

while True:
    IO.output(LED_PIN, IO.HIGH)
    time.sleep(DELAY)
    IO.output(LED_PIN, IO.LOW)
    time.sleep(DELAY)