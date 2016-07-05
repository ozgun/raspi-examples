# Turn on/off a LED

import RPi.GPIO as GPIO
from time import sleep

# GPIO(BCM) numbering. See README.
# BCM - Broadcom pin number, commonly called "GPIO".
GPIO.setmode(GPIO.BCM)

led_pin = 4

try:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, True)
    sleep(5)
    GPIO.output(led_pin, False)
finally:
    # Reset the GPIO pins to a safe state
    GPIO.cleanup()
