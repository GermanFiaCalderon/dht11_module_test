import Adafruit_DHT
import json
import I2C_LCD_driver
import time
import RPi.GPIO as GPIO
import sqlite3
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

pantallalcd = I2C_LCD_driver.lcd()
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

connection = sqlite3.connect("Data.db")
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS data;")
time.sleep(0.2)
cursor.execute("CREATE TABLE data (Temp TEXT, Hume TEXT )")

with open("Config.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

a = 1
while a < 10:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        pantallalcd.lcd_display_string("Temp={0:0.1f}C ".format(temperature, humidity), 1)
        pantallalcd.lcd_display_string("Hume={1:0.1f}%".format(temperature, humidity), 2)
        #print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        GPIO.output(16,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(16,GPIO.LOW)

        cursor.execute("INSERT INTO data VALUES ('{0:0.1f}C', '{1:0.1f}%')".format(temperature, humidity))
      
        time.sleep(datos_json["tiempo"])

        
    else:
        print("Sensor failure. Check wiring.");
        time.sleep(1);
        
    
with open("Config.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

b = 1
while b < 10:
   humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
   if True:
        cursor.execute("INSERT INTO data VALUES ('{0:0.1f}C', '{1:0.1f}%')".format(temperature, humidity))
        rows = cursor.execute("SELECT Temp, Hume FROM data").fetchall()
        print(rows)
        time.sleep(datos_json["send_data"])
       