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
        led.value = True    # if object is tilted 90 degrees turn the led on