# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [launch pad part 1](#launch_pad_part_1)
* [launch pad part 2](#launch_pad_part_2)
* [launch pad part 3](#launch_pad_part_3)
* [launch pad part 4](#launch_pad_part_4)
* [crash avoidance part 1](#crash_avoidance_part_1)
* [crash avoidance part 2](#crash_avoidance_part_2)
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

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

[test.py](raspberry-pi/test.py) ![Rotating_earth_(large)](https://github.com/Cooper-Moreland/Engineering_4_Notebook/assets/71406906/2f8658ea-5f2d-4c27-823a-6129dda746b8)![tree-736885_1280](https://github.com/Cooper-Moreland/Engineering_4_Notebook/assets/71406906/8525bdf9-da0a-4325-b4ea-236d2c498c46)
