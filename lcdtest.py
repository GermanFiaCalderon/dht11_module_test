import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()
import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)


while True:
    mylcd.lcd_display_string("Hora: %s" %time.strftime("%H:%M:%S"), 1)
    
    mylcd.lcd_display_string("Fecha:%s" %time.strftime("%m/%d/%Y"), 2)

    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.5)

    