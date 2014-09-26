import RPi.GPIO as GPIO
import time

pinNum = 7 

GPIO.setmode(GPIO.BOARD) # Set to board mode
GPIO.setup(pinNum,GPIO.OUT)

# Goes into an inifinite loop to flash the LED light bulb
while True:
  GPIO.output(pinNum,GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(pinNum,GPIO.LOW)
  time.sleep(0.5)     

