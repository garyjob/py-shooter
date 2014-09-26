# Py-Shooter

Test project to interface Raspberry Pi a DC motor via Python

## Setting up 
#### Setting up a the breadboard
![Alt text](/imgs/breadboard.png "breadboard overview")

https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/breadboard/

#### Installing the environment dependencies in Raspberry PI
https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/downloads/

# When using GPIO.BOARD the pinNum goes from 1 - 26 as depicted in the circles
```python
pinNum = 7
GPIO.setmode(GPIO.BOARD) # Set to board mode
GPIO.setup(pinNum,GPIO.OUT)

GPIO.output(pinNum,GPIO.HIGH) # Turn on 
GPIO.output(pinNum,GPIO.LOW) # Turn off
```