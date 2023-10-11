# dht11_module_test

Utilizar sensor DHT11 para hacer leer temperatura y humedad.

guardar en un archivo de configuracion de formato JSON dos parámetros (tiempo y send_data)

el tiempo debe ser el delay que se le aplique a la lectura de temp y de hume.

Cada vez que se realize una lectura se debe guardar en una base de datos, con una tabla que contenga cada dato registrado.

Una vez se cumplio el tiempo de "send_data" la base de datos se debe imprimir en la terminal y despues borrarse o hacer un clear automaticamente.

MATERIALES:

Led RGB (se debe prender cada vez que se hace una lectura).
DISPLAY I2C LCD (debe decir "Data Cleared cada vez que se borra la base de datos)
SENSOR DHT11

LIBRERIAS:
Sqlite
Gpio
json
