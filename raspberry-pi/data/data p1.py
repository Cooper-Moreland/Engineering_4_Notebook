# type: ignore
# libraries: adafruit_mpu6050.mpy | adafruit_bus_device | adafruit_register
import adafruit_mpu6050
import busio
import board
import time
import digitalio
import displayio
import storage

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
    acc = mpu.acceleration
    print(f"X: {acc[0]}m/s² Y: {acc[1]}m/s² Z: {acc[2]}m/s²")
    time.sleep(0.5)
    led1.value = False
    if abs(acc[2]) < 2:
        led1.value = True
    if not storage.getmount("/").readonly:
        # we can write to the filesystem
        with open("/data.csv", "a") as datalog:
            written_string = f"{time.monotonic()},{acc[0]},{acc[1]},{acc[2]},{tilt_led.value}\n"
            datalog.write(written_string)
            datalog.flush()
            # blink onboard LED to indicate activity
            led2.value = True
            time.sleep(0.25)
            led2.value = False
            time.sleep(0.25)
    else:
        # sleep anyways
        time.sleep(0.25)