import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16,GPIO.HIGH)
time.sleep(5.0)
GPIO.output(16,GPIO.LOW)