# Turn on/off a LED
#
# $ sudo python3 led_on_off_BOARD.py

import RPi.GPIO as GPIO
from time import sleep

# Physical numbering. See README.
GPIO.setmode(GPIO.BOARD)

led_pin = 7

try:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, True)
    sleep(3)
    GPIO.output(led_pin, False)
finally:
    # Reset the GPIO pins to a safe state
    GPIO.cleanup()
