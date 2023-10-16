import Adafruit_DHT
import json
import I2C_LCD_driver
import time
import RPi.GPIO as GPIO
import sqlite3
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
#asigna la variable de la pantalla lcd
pantallalcd = I2C_LCD_driver.lcd()
#selecciona el tipo de sensor
DHT_SENSOR = Adafruit_DHT.DHT11
#selecciona el pin del sensor
DHT_PIN = 4
#hace la coneccion con la base de datos
connection = sqlite3.connect("Data.db")
print(connection.total_changes)
#asigna la variable de configuracion con el sensor
cursor = connection.cursor()
#se encarga de limpiar la base de datos por si se encontraba sucia
cursor.execute("DROP TABLE IF EXISTS data;")
time.sleep(0.2)
cursor.execute("CREATE TABLE data (Temp TEXT, Hume TEXT )")
#abre el archivo de configuracion json
with open("Config.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

a = 1
while a < 10:
    #se consulta el sensor 
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        #se escribe en la pantalla lcd los datos
        pantallalcd.lcd_clear()
        pantallalcd.lcd_display_string("Temp={0:0.1f}C ".format(temperature, humidity), 1)
        pantallalcd.lcd_display_string("Hume={1:0.1f}%".format(temperature, humidity), 2)
        #print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        #el led se enciende con cada lectura
        GPIO.output(16,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(16,GPIO.LOW)
        #se escribe los datos en la base de datos
        cursor.execute("INSERT INTO data VALUES ('{0:0.1f}C', '{1:0.1f}%')".format(temperature, humidity))
      
        time.sleep(datos_json["tiempo"])
    #avisa si no se leyo el dato
    else:
        print("Sensor failure. Check wiring.")
        time.sleep(1)

    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if True:
       #escribe la base de datos en el terminal
        rows = cursor.execute("SELECT Temp, Hume FROM data").fetchall()
        print(rows)
        pantallalcd.lcd_clear()
        pantallalcd.lcd_display_string("Data Cleared", 1, 2)
        #lipia la tabla
        cursor.execute("DROP TABLE IF EXISTS data;")
        time.sleep(0.2)
        cursor.execute("CREATE TABLE data (Temp TEXT, Hume TEXT )")
        time.sleep(datos_json["send_data"])

     
        
    
