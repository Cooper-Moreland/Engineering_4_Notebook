# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [launch pad part 1](#launch_pad_part_1)
* [launch pad part 2](#launch_pad_part_2)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## launch_pad_part_1

### Description

You need to countdown from 10 seconds down to Liftoff (at 0 seconds). That countdown must be printed to the serial monitor.

### Evidence 

```python
# type: ignore
import time
import board

for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
    print(x) # print the variable
    time.sleep(1.0) # delay of 1 sec
print("LIFTOFF!")

```

### Wiring

N/A 

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/2-1%20countdown.py)

### Reflection

helpful [link](https://www.w3schools.com/python/gloss_python_for_range.asp) for the type of code you need for this assignment.

https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-07%20135157.png?raw=true

## launch_pad_part_2

### Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.

### Evidence 

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

### Wiring

![1](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/Screenshot%202023-09-07%20135157.png?raw=true)

### [Code](https://github.com/Cooper-Moreland/Engineering_4_Notebook/blob/main/raspberry-pi/2-2%20countdown.py)

### Reflection

long led leg is (+) short leg is (-), use a 10k resistor so you don't blind yourself.

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


### Test Link

### Test Image

### Test GIF
