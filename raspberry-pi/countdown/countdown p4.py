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