# type: ignore
# libraries: adafruit_mpu6050.mpy | adafruit_bus_device | adafruit_register
import adafruit_mpu6050
import busio
import board
import time
import digitalio
import displayio
import storage # imports

displayio.release_displays() # this needs to be first in the code

led1 = digitalio.DigitalInOut(board.GP16) 
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.LED)
led2.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
mpu = adafruit_mpu6050.MPU6050(i2c) # set up for variables and pin locations

while True: 
    acc = mpu.acceleration # new var
    print(f"X: {acc[0]}m/s² Y: {acc[1]}m/s² Z: {acc[2]}m/s²") # f string for accel of the breadboard
    time.sleep(0.25)
    led1.value = False # default led is off
    if abs(acc[2]) < 2:
        led1.value = True # when tilted sideway turn the led on 
    if not storage.getmount("/").readonly: # call back to the boot.py file
        with open("/data.csv", "a") as datalog:
            time_elapsed = time.monotonic()
            csv_string = f"{time_elapsed},{acc[0]},{acc[1]},{acc[2]},{led1.value}\n"
            # f string showing time, acc, and whether or not it's tilted
            datalog.write(csv_string)
            led2.value = True
            time.sleep(0.1)
            led2.value = False
            time.sleep(0.1) # blink led to show switch between modes
            datalog.flush() # record stuff to the datalog
            time.sleep(0.25)
    else:
        time.sleep(0.25)