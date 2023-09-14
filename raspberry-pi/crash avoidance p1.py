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
    accleration = mpu.acceleration # new var
    print(f"X: {acceleration[0]} m/s^2 Y: {acceleration[1]} m/s^2 Z: {acceleration[1]} m/s^2") # print x, y, and z values
    time.sleep(0.25) # debounce
