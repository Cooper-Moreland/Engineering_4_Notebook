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