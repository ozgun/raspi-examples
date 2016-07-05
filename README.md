Pyhton &amp; Ruby code samples for **Raspberry Pi 2**

### Operating System

**Raspbian GNU/Linux 8** is installed on my **Raspberry Pi 2 Model B**.

### Install C, Python and Ruby Libraries

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install wiringpi
```

```
$ sudo apt-get install python-dev python-pip
$ sudo pip install RPi.GPIO
```

```
$ sudo apt-get install ruby-dev libssl-dev
$ sudo gem install pi_piper
```

### Running Examples

Most of the examples found in this repo should be run as root.

```
$ sudo python3 python/led_on_off_BCM.py
$ sudo ruby ruby/led_on_off.rb
$ ./shell/led_on_off_with_gpio_utility.rb
```

### BCM(GPIO) vs Physical vs WiringPi Numbering

* **BCM(GPIO)** - Broadcom pin number, commonly called "GPIO", these are the ones you probably want to use with RPi.GPIO and GPIO Zero
* **WiringPi** - Wiring Pi pin number (shown as a tooltip), for Gordon's Wiring Pi library
* **Physical** - Number corresponding to the pin's physical location on the header

### The GPIO Utility

See https://projects.drogon.net/raspberry-pi/wiringpi/the-gpio-utility/

"The gpio command is designed to be installed as a setuid program and called by
a normal user without using the sudo command or logging in as root."

```
$ gpio readall
```

Output:

```
+-----+-----+---------+------+---+---Pi 2---+---+------+---------+-----+-----+
| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
|     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
|   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5V      |     |     |
|   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
|   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT0 | TxD     | 15  | 14  |
|     |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 16  | 15  |
|  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
|  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
|  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
|     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
|  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
|   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
|  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
|     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
|   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
|   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
|   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
|  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
|  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
|  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
|     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
+-----+-----+---------+------+---+---Pi 2---+---+------+---------+-----+-----+
```

### Links

#### Libraries

* [The wiringPi libraries, headers and gpio command](https://projects.drogon.net/raspberry-pi/wiringpi/)
* [RPi.GPIO Python Module](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
* [pi_piper Ruby Gem](https://github.com/jwhitehorn/pi_piper/)

#### Tutorials & Code Samples & Documents

* [GPIO Pinout Guide for Raspberry Pi Models](http://pinout.xyz/)
* [An Introduction to GPIO and Physical Computing on the Raspberry Pi](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/)
* [Alexander Baran-Harper - YouTube Channel](https://www.youtube.com/channel/UC_aQTJgfrnCb8coPbZ5cgJw)
* [Raspi.TV](http://raspi.tv/)

