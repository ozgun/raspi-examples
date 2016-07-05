# The optional -g flag causes pin numbers to be interpreted as BCM_GPIO pin
# numbers rather than standard wiringPi pin numbers.
#
# NOTE: Run this script as root

gpio -g mode 4 out
gpio -g read 4
gpio -g write 4 1
gpio -g read 4
gpio -g write 4 0
gpio -g read 4
