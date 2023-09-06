# type: ignore
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
    print(x) # print the variable
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
print("LIFTOFF!")