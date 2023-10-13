import os

# Ruta del archivo que deseas eliminar
archivo_a_eliminar = "/home/developer/Desktop/Proyectosensor/Data.db"

# Verificar si el archivo existe antes de eliminarlo
if os.path.exists(archivo_a_eliminar):
    # Eliminar el archivo
    os.remove(archivo_a_eliminar)
    print("Archivo eliminado con éxito.")
else:
    print("El archivo no existe.")