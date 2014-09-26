import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # Set to board mode
GPIO.setup(pinNum,GPIO.OUT)

pinNum = 7 

# Goes into an inifinite loop to flash the LED light bulb
while True:
  GPIO.output(pinNum,GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(pinNum,GPIO.LOW)
  time.sleep(0.5)     

