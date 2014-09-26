# Py-Shooter

Test project to interface Raspberry Pi a DC motor via Python

## Setting up 
#### Setting up a the breadboard
![Alt text](/imgs/breadboard.png "breadboard overview")

https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/breadboard/

#### Connecting
- The Positive of a component always is connected with where the voltage is coming from
- The Negative end of the component always is connected with where the grounding goes

###### Sample close circuit
- GPI04 -> Postive Light Bulb , Negative Light Bulb -> GND


#### Installing the environment dependencies in Raspberry PI
https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/downloads/

## Usage
When using GPIO.BOARD the pinNum goes from 1 - 26 as depicted in the circles
```python
pinNum = 7 # GPI04
GPIO.setmode(GPIO.BOARD) # Set to board mode
GPIO.setup(pinNum,GPIO.OUT)

GPIO.output(pinNum,GPIO.HIGH) # Turn on 
GPIO.output(pinNum,GPIO.LOW) # Turn off
```