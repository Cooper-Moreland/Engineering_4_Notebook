# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [launch pad part 1](#launch_pad_part_1)
* [launch pad part 2](#launch_pad_part_2)
* [launch pad part 3](#launch_pad_part_3)
* [launch pad part 4](#launch_pad_part_4)
* [crash avoidance part 1](#crash_avoidance_part_1)
* [crash avoidance part 2](#crash_avoidance_part_2)
* [crash avoidance part 3](#crash_avoidance_part_3)
* [beam_starter](#beam_starter) 
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## launch_pad_part_1

### Description

You need to countdown from 10 seconds down to Liftoff (at 0 seconds). That countdown must be printed to the serial monitor.

### Evidence 

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/launchpadp1.gif?raw=true)

### Wiring

N/A 

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/2-1%20countdown.py)

```python
# type: ignore
import time
import board

for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
    print(x) # print the variable
    time.sleep(1.0) # delay of 1 sec
print("LIFTOFF!")

```

### Reflection

helpful [link](https://www.w3schools.com/python/gloss_python_for_range.asp) for the type of code you need for this assignment. to upload a video download the video go to [ezgif.com/video-to-gif](ezgif.com/video-to-gif) upload the video then convert to gif upload that gif to githib and copy the link address. then use the code line "![anthing here](here goes the link address)"

## launch_pad_part_2

### Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.

### Evidence/Video

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/launchpadp2.gif?raw=true)

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-07%20135157.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/2-2%20countdown.py)

```python
# type: ignore
import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.GP16)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP17)
led2.direction = digitalio.Direction.OUTPUT # red and green led output location

for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
    print(x) # print the variable
    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5) # blink red led
print("LIFTOFF!")
led2.value = True
time.sleep(5.0) # green led on for 5 secs

```

### Reflection

long led leg is (+) short leg is (-), use a 10k resistor so you don't blind yourself. New board pin placements are new to learn but they mostly just go in a u formation starting at the top left and going from GP1 to GPwhateverthelastnumberis.

## launch_pad_part_3

### Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff. Include a physical button that starts the countdown.

### Evidence/Video

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/launchpadp3.gif?raw=true)

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-11%20134841.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/countdown%20p3.py)

```python
# type: ignore
import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

led1 = digitalio.DigitalInOut(board.GP16)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP17)
led2.direction = digitalio.Direction.OUTPUT # red and green led output location

btn = DigitalInOut(board.GP15)
btn.direction = Direction.INPUT
btn.pull = Pull.UP # set pin number and input as pull up

prev_state = btn.value # new variable

while True:
    cur_state = btn.value # new variable
    if cur_state != prev_state: # if the state of the button changes
        if not cur_state: # if the button is pressed
            print("BTN is down")
            for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
                print(x) # print the variable
                led1.value = True
                time.sleep(0.5)
                led1.value = False
                time.sleep(0.5) # blink red led
            led2.value = True 
            print("LIFTOFF!")
            time.sleep(3.0)
            led2.value = False # turn on green light and print liftoff then turn the light off after 3 seconds
        else:
            print("BTN is up")

    prev_state = cur_state # reset button value

```

### Reflection

[useful page](https://learn.adafruit.com/multi-tasking-with-circuitpython/buttons) for figuring out how to code button presses. If you use pull.up the default value for the button is true and you wire it to ground and a pin number. If you use pull.down defualt value is false and you wire it to 3v3 and the pin number.

## launch_pad_part_4

### Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff. Include a physical button that starts the countdown. Actuate a 180-degree servo on liftoff to simulate the launch tower disconnecting.

### [Evidence/Video](https://photos.app.goo.gl/PXsUUYmJFtQ5w9Ju9)

![servogif](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/servogif.gif?raw=true)

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/launch_pad_part_4.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/countdown%20p4.py)

```python
# type: ignore
import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

led1 = digitalio.DigitalInOut(board.GP16)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP17)
led2.direction = digitalio.Direction.OUTPUT # red and green led output location

btn = DigitalInOut(board.GP15)
btn.direction = Direction.INPUT
btn.pull = Pull.UP # set pin number and input as pull up

pwm = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=50) #placeholder for whatever pin I choose
my_servo = servo.Servo(pwm)

prev_state = btn.value # new variable

while True:
    cur_state = btn.value # new variable
    if cur_state != prev_state: # if the state of the button changes
        if not cur_state: # if the button is pressed
            print("BTN is down")
            for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
                print(x) # print the variable
                led1.value = True
                time.sleep(0.5)
                led1.value = False
                time.sleep(0.5) # blink red led
            led2.value = True # turn on green led
            print("LIFTOFF!")
            for angle in range(0, 180, 1):  # 0 - 180 degrees, 1 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.01)
            time.sleep(3.0)
            led2.value = False # turn on green light and print liftoff then turn the light off after 3 seconds
            for angle in range(180, 0, -1):  # 180 - 0 degrees, 1 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.01) # reset servo
        else:
            print("BTN is up")

    prev_state = cur_state # reset button value to unpressed

```

### Reflection

Download [8.x](https://circuitpython.org/libraries) python library to use imports like servo, this one is in adafruit_motor. Every GP pin on the Pico is capable of PWM, but there is one catch. Some of the pins run on the same PWM channels, and you can only use one pin on the channel. For example, if I am driving one servo with board.GP0, I cannot drive a second servo with board.GP16, because they both use the PWM_A[0] channel, check [this](https://www.codrey.com/wp-content/uploads/2021/09/Raspberry-Pi-Pico-PWM-Pins.jpg) to see if the pins pwms overlap.

## crash_avoidance_part_1

### Description

The module must have an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor.

### [Evidence/Video](https://photos.app.goo.gl/STigwdacgecz1s276)

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/accel.gif?raw=true)

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-15%20133802.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/crash%20avoidance%20p1.py)

```python
# type: ignore
import adafruit_mpu6050
import busio
import board
import time

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
mpu = adafruit_mpu6050.MPU6050(i2c) # set up for variables and pin locations

while True:
    acc = mpu.acceleration # new var
    print(f"X: {acc[0]} m/s^2 Y: {acc[1]} m/s^2 Z: {acc[2]} m/s^2") # print x, y, and z values
    time.sleep(0.75) # debounce

```

### Reflection

[google doc for assignment](https://docs.google.com/document/d/1g1PIIIek534bj5pJsN9bA1CqbQQEbnUsOCIuNnpgo2o/edit). The [Pico](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2021/01/raspberry_pi_pico_pinout.png) has a bunch of pins that can be used for I2C. Any of the blue labeled pins are I2C capable, but you must ensure that the SCL and SDA pins (labeled in blue) you use are from the same I2C bus.

## crash_avoidance_part_2

### Description

The module must have an accelerometer that continuously reports x, y, and z acceleration values. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source.

### Evidence/Video

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/crashavoidancep2.gif?raw=true)

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-22%20133132.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/crash%20avoidance%20p2.py)

```python
# type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio

led = digitalio.DigitalInOut(board.GP0) 
led.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
mpu = adafruit_mpu6050.MPU6050(i2c) # set up for variables and pin locations

while True:
    acc = mpu.acceleration # new var
    print(f"X: {acc[0]} m/s^2 Y: {acc[1]} m/s^2 Z: {acc[2]} m/s^2") # print x, y, and z values
    time.sleep(0.75) # debounce
    led.value = False # default led is off
    if acc[0] > 9 or acc[0] < -9:
        print("mayday")
        led.value = True    # if object is tilted 90 or -90 degrees turn the led on

```

### Reflection

WeVideo can capture the screen and record on a camera at the same time which is useful for showing the serial monitor. The new lines of code are just an if statement 9 and -9 correspond to 90 and -90 degrees which is something to remember if I need to do this again. GND to GND and Sw to 3v3 for the new battery thing to power the Raspberry Pico. [link for this assignment](https://docs.google.com/document/d/1aIv2ZZ7GjsV_WlQ2PhkF72Qr4De23a8TKEGw4vXBKfE/edit?usp=sharing)

## crash_avoidance_part_3

### Description

The module must have an accelerometer that continuously reports x, y, and z acceleration values. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source. The module must have an onboard screen that prints x, y, and z angular velocity values (rad/s) rounded to 3 decimal places.

### Evidence/Video

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/crashavoidancep3.gif?raw=true)

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-26%20125639.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/crash%20avoidance%20p3.py)

```python
# type: ignore
# libraries: adafruit_displayio_ssd1306.mpy | adafruit_display_text | adafruit_mpu6050.mpy | adafruit_bus_device | adafruit_register
import time
import adafruit_mpu6050
import busio
import board
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import digitalio
import terminalio
import displayio

displayio.release_displays() # this needs to be first in the code

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # set up for variables and pin locations

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP21)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # pin address and setup for oled display

led = digitalio.DigitalInOut(board.GP0) 
led.direction = digitalio.Direction.OUTPUT

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

# send display group to screen
display.show(splash)

while True:
    acc = mpu.acceleration # new var
    print(f"X: {acc[0]} m/s^2 Y: {acc[1]} m/s^2 Z: {acc[2]} m/s^2") # print x, y, and z values
    gyro = mpu.gyro # new var for gyro
    text_area.text = f"X: {gyro[0]: .3f}rad/s\nY: {gyro[1]: .3f}rad/s\nZ: {gyro[2]: .3f}rad/s"  # print the values on the oled display, .3f means 3 decimal point
    # \n breaks the line and goes to next row for the following text
    time.sleep(0.75) # debounce
    led.value = False # default led is off
    if acc[0] > 8 or acc[0] < -8:
        print("mayday")
        led.value = True    # if object is tilted 90 or -90 degrees turn the led on

```

### Reflection

breadboards can connect to each other for more space. on the oled screen Clk goes to scl, Data goes to sda, reset pin can go to any random GP. Make sure the external battery is fully pugged in so it doesn't fry your board, but if that happens uninstall circuit python from vs code then reinstall.

&nbsp;

## beam_starter

### Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### [Onshape Link](https://cvilleschools.onshape.com/documents/a4035a22ba64776340356020/w/11ed539d4eb836d893f3062b/e/6c6a605be107bca51b691821?renderMode=0&uiState=651c472fb79d590382eddea4)

### Part Image

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-10-03%20125101.png?raw=true)

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

## Onshape_Assignment_Template

### Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### [Onshape Link](

### Part Image

![1](

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

[test.py](raspberry-pi/test.py) ![Rotating_earth_(large)](https://github.com/Cooper-Moreland/Engineering_4_Notebook/assets/71406906/2f8658ea-5f2d-4c27-823a-6129dda746b8)![tree-736885_1280](https://github.com/Cooper-Moreland/Engineering_4_Notebook/assets/71406906/8525bdf9-da0a-4325-b4ea-236d2c498c46)
