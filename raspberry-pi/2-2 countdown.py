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