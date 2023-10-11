import time
import board
import adafruit_dht
import json

#Pin del sensor
dhtDevice = adafruit_dht.DHT11(board.D21)
#consulta el archivo json
with open("Config.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

while True:
    #Intenta acceder al dato del sensor dht11
    try:
        #lee la temperatura en centigrados
        temperature_c = dhtDevice.temperature
        #convierte la temperatura de centigrados a fahrenheit
        temperature_f = temperature_c*(9 / 5)+32
        #lee la humedad que detecta el sensor
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature_f} F / {temperature_c} C     Humedad:{humidity}%")
        time.sleep(type(datos_json))
        time.sleep(datos_json["tiempo"])
        

    #En caso de error escribe el error en pantalla
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)    
