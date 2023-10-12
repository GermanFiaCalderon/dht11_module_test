import json
import I2C_LCD_driver
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

pantallalcd = I2C_LCD_driver.lcd()

with open("Config.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

while True:
    pantallalcd.lcd_display_string("Hora: %s" %time.strftime("%H:%M:%S"), 1)
    
    pantallalcd.lcd_display_string("Fecha:%s" %time.strftime("%m/%d/%Y"), 2)
    time.sleep(1.0)

    while True:
        GPIO.output(16,GPIO.HIGH)
        time.sleep(datos_json["tiempo"])
        GPIO.output(16,GPIO.LOW)
        time.sleep(0.5)
