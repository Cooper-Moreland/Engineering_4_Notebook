#type: ignore
import time
import terminalio
import displayio
import busio    
import board
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line

displayio.release_displays() #display

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) #sda and scl pin for oled

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP21)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #oled setup and address

splash = displayio.Group() #display group creation

splash.append(Circle(64, 32, 3, outline=0xFFFFFF))
splash.append(Line(0, 32, 128, 32, 0xFFFFFF))
splash.append(Line(64, 0, 64, 64, 0xFFFFFF)) #add base and coordinate axes
area_label = label.Label(terminalio.FONT, x=5, y=5, text="")
splash.append(area_label)
landing_area_display = None #splash.append(Triangle(5, 5, 30, 30, 10, 30, outline=0xFFFFFF))

display.show(splash) #display group and screen communication

def validate_input(input_string: str): # return false on error or an array of the form [x, y] on success
    try:
        input_parts = input_string.split(",")
    except ValueError:
        return False
    if len(input_parts) != 2: # we expect an x and a y coordinate
        return False
    try:
        result = [float(part) for part in input_parts] # turn the strings in input_parts into floats
        return result
    except ValueError: # if something wasn't a float
        return False

def get_area(p1, p2, p3): 
    area = 0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) # math equation for area
    return abs(area)

while True:
    vertex_1 = validate_input(input("Vertex 1: "))
    if not vertex_1:
        print("That was not the proper format. Please try again.")
        continue
    vertex_2 = validate_input(input("Vertex 2: "))
    if not vertex_2:
        print("That was not the proper format. Please try again.")
        continue
    vertex_3 = validate_input(input("Vertex 3: "))
    if not vertex_3:
        print("That was not the proper format. Please try again.")
        continue
    area = get_area(vertex_1, vertex_2, vertex_3) #plug points into area equation
    print(f"The area of the triangle with vertices ({vertex_1[0]},{vertex_1[1]}), ({vertex_2[0]},{vertex_2[1]}), ({vertex_3[0]},{vertex_3[1]}) is {area} square km.") 
    #f string printing coords and value of area in km^2
    area_label.text = f"{area:.2f}km2" # set the text that shows on the display
    if landing_area_display is not None: # erase previous triangle
        splash.pop()
    landing_area_display = Triangle(int(vertex_1[0])+64, 32-int(vertex_1[1]), int(vertex_2[0])+64, 32-int(vertex_2[1]), int(vertex_3[0])+64, 32-int(vertex_3[1]), outline=0xFFFFFF)
    # place (0,0) at the center of the screen and make the axis lines white
    splash.append(landing_area_display) # show the triangle on the oled screen