# Turn on/off a LED

require 'pi_piper'

# "pin" refers to the GPIO(BCM) number of the Raspberry Pi.
# See README.
pin = PiPiper::Pin.new(:pin => 4, :direction => :out)

puts pin.read # => 0
pin.on
puts pin.read # => 1

sleep 3

pin.off
puts pin.read # => 0
